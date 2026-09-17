# Hash-bound customization support for the native PowerShell installer.
function Get-BytesHash {
    param([byte[]]$Bytes)
    $sha = [System.Security.Cryptography.SHA256]::Create()
    try { return ([BitConverter]::ToString($sha.ComputeHash($Bytes))).Replace('-', '').ToLowerInvariant() }
    finally { $sha.Dispose() }
}

function Set-SkillCustomization {
    param([string]$Source, [string]$DestinationName, $Spec)
    $prefix = $DestinationName + '/'
    $root = [System.IO.Path]::GetFullPath($Source).TrimEnd('\', '/') + [System.IO.Path]::DirectorySeparatorChar
    $pending = @()
    foreach ($entry in $Spec.files) {
        if (-not $entry.path.StartsWith($prefix, [StringComparison]::Ordinal)) { continue }
        $relative = $entry.path.Substring($prefix.Length)
        if ($relative -match '(^/|(^|/)\.\.(/|$)|[:\\])') { throw "Unsafe customization path: $relative" }
        $target = [System.IO.Path]::GetFullPath((Join-Path $Source $relative))
        if (-not $target.StartsWith($root, [StringComparison]::OrdinalIgnoreCase)) { throw "Customization escapes root: $relative" }
        $bytes = [System.IO.File]::ReadAllBytes($target)
        $hash = Get-BytesHash $bytes
        if ($hash -eq $entry.after_sha256) { continue }
        if ($hash -ne $entry.before_sha256) { throw "Content changed; review before customizing: $($entry.path)" }
        $text = [System.Text.Encoding]::UTF8.GetString($bytes).TrimStart([char]0xfeff).Replace("`r`n", "`n")
        foreach ($name in $entry.rules) {
            $rule = $Spec.rules.PSObject.Properties[$name].Value
            switch ($rule.op) {
                'file' { $text = $rule.text }
                'replace' {
                    $count = if ($null -ne $rule.count) { $rule.count } else { 1 }
                    if ([regex]::Matches($text, [regex]::Escape($rule.old)).Count -ne $count) { throw "Ambiguous replacement: $name" }
                    $text = $text.Replace($rule.old, $rule.text)
                }
                'span' {
                    if ([regex]::Matches($text, [regex]::Escape($rule.start)).Count -ne 1) { throw "Ambiguous span: $name" }
                    $start = $text.IndexOf($rule.start, [StringComparison]::Ordinal)
                    $end = $text.IndexOf($rule.end, $start, [StringComparison]::Ordinal)
                    if ($end -lt 0) { throw "Missing end marker: $name" }
                    if ($rule.include_end) { $end += $rule.end.Length }
                    $text = $text.Substring(0, $start) + $rule.text + $text.Substring($end)
                }
                default { throw "Unknown customization operation: $($rule.op)" }
            }
        }
        $newBytes = [System.Text.Encoding]::UTF8.GetBytes($text)
        if ((Get-BytesHash $newBytes) -ne $entry.after_sha256) { throw "Customization result mismatch: $($entry.path)" }
        $pending += @{ Path = $target; Bytes = $newBytes }
    }
    foreach ($entry in $pending) { [System.IO.File]::WriteAllBytes($entry.Path, $entry.Bytes) }
}
