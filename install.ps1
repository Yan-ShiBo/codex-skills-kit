param(
    [switch]$Latest,
    [switch]$Force,
    [switch]$SkipPlugins,
    [string]$CodexHome
)

$ErrorActionPreference = "Stop"
$RawBase = "https://raw.githubusercontent.com/Yan-ShiBo/codex-skills-kit/main"

function Get-WithRetry {
    param(
        [Parameter(Mandatory = $true)][string]$Uri,
        [Parameter(Mandatory = $true)][string]$OutFile
    )

    $lastError = $null
    foreach ($attempt in 1..3) {
        try {
            Invoke-WebRequest -Uri $Uri -OutFile $OutFile -UseBasicParsing
            return
        } catch {
            $lastError = $_
            if ($attempt -lt 3) {
                Start-Sleep -Seconds ($attempt * 2)
            }
        }
    }
    throw "Failed to download $Uri`: $lastError"
}

function Copy-SkillDirectory {
    param(
        [Parameter(Mandatory = $true)][string]$Source,
        [Parameter(Mandatory = $true)][string]$Destination,
        [switch]$Replace
    )

    if (Test-Path -LiteralPath $Destination) {
        if (-not $Replace) {
            return "skipped"
        }
        $timestamp = Get-Date -Format "yyyyMMdd-HHmmss"
        $backup = "$Destination.backup-$timestamp"
        Move-Item -LiteralPath $Destination -Destination $backup
    }
    Copy-Item -LiteralPath $Source -Destination $Destination -Recurse
    return "installed"
}

if ([string]::IsNullOrWhiteSpace($CodexHome)) {
    if (-not [string]::IsNullOrWhiteSpace($env:CODEX_HOME)) {
        $CodexHome = $env:CODEX_HOME
    } else {
        $CodexHome = Join-Path $HOME ".codex"
    }
}

$CodexHome = [System.IO.Path]::GetFullPath($CodexHome)
$SkillsRoot = Join-Path $CodexHome "skills"
New-Item -ItemType Directory -Path $SkillsRoot -Force | Out-Null

$localManifest = if ($PSScriptRoot) {
    Join-Path $PSScriptRoot "manifest\install-manifest.json"
} else {
    $null
}

$tempRoot = Join-Path ([System.IO.Path]::GetTempPath()) ("codex-skills-" + [guid]::NewGuid())
New-Item -ItemType Directory -Path $tempRoot | Out-Null

try {
    if ($localManifest -and (Test-Path -LiteralPath $localManifest)) {
        $manifest = Get-Content -Raw -LiteralPath $localManifest | ConvertFrom-Json
    } else {
        $manifestPath = Join-Path $tempRoot "install-manifest.json"
        Get-WithRetry "$RawBase/manifest/install-manifest.json" $manifestPath
        $manifest = Get-Content -Raw -LiteralPath $manifestPath | ConvertFrom-Json
    }

    $installed = 0
    $skipped = 0
    $failed = 0

    foreach ($package in $manifest.sources) {
        $parts = $package.source.Split("/", 2)
        $owner = $parts[0]
        $repo = $parts[1]
        $ref = if ($Latest) { "main" } else { $package.ref }
        Write-Host "`n[$($package.source)] ref=$ref"

        $pending = @()
        foreach ($item in $package.items) {
            $destination = Join-Path $SkillsRoot $item.destination
            if ((Test-Path -LiteralPath $destination) -and -not $Force) {
                Write-Host ("  {0,-9} {1} -> {2}" -f "SKIPPED", $item.name, $destination)
                $skipped++
            } else {
                $pending += $item
            }
        }
        if ($pending.Count -eq 0) {
            continue
        }

        $packageRoot = Join-Path $tempRoot ([guid]::NewGuid().ToString())
        New-Item -ItemType Directory -Path $packageRoot | Out-Null
        $archive = Join-Path $packageRoot "source.zip"
        $expanded = Join-Path $packageRoot "expanded"

        try {
            $singleFileItems = @($pending | Where-Object { $_.single_file })
            if ($singleFileItems.Count -eq $pending.Count) {
                foreach ($item in $pending) {
                    $sourcePath = Join-Path $packageRoot $item.name
                    New-Item -ItemType Directory -Path $sourcePath | Out-Null
                    $relative = "$($item.source_path.TrimEnd('/'))/$($item.single_file)"
                    Get-WithRetry "https://raw.githubusercontent.com/$($package.source)/$ref/$relative" (Join-Path $sourcePath $item.single_file)
                    $destination = Join-Path $SkillsRoot $item.destination
                    $result = Copy-SkillDirectory -Source $sourcePath -Destination $destination -Replace:$Force
                    Write-Host ("  {0,-9} {1} -> {2}" -f $result.ToUpperInvariant(), $item.name, $destination)
                    if ($result -eq "installed") { $installed++ } else { $skipped++ }
                }
                continue
            }

            Get-WithRetry "https://codeload.github.com/$owner/$repo/zip/$ref" $archive
            Expand-Archive -LiteralPath $archive -DestinationPath $expanded
            $roots = @(Get-ChildItem -LiteralPath $expanded -Directory)
            if ($roots.Count -ne 1) {
                throw "Unexpected GitHub archive layout"
            }
            $root = $roots[0].FullName

            foreach ($item in $pending) {
                $sourcePath = if ($item.source_path -eq ".") {
                    $root
                } else {
                    Join-Path $root ($item.source_path.Replace("/", "\"))
                }
                $destination = Join-Path $SkillsRoot $item.destination
                if (-not (Test-Path -LiteralPath $sourcePath -PathType Container)) {
                    Write-Warning "Missing $($item.source_path) for $($item.name)"
                    $failed++
                    continue
                }
                $result = Copy-SkillDirectory -Source $sourcePath -Destination $destination -Replace:$Force
                Write-Host ("  {0,-9} {1} -> {2}" -f $result.ToUpperInvariant(), $item.name, $destination)
                if ($result -eq "installed") { $installed++ } else { $skipped++ }
            }
        } catch {
            Write-Warning "Package failed: $($_.Exception.Message)"
            $failed += $pending.Count
        }
    }

    Write-Host "`nSkills complete: installed=$installed, skipped=$skipped, failed=$failed"
    if ($failed -gt 0) {
        throw "$failed skill items failed"
    }

    if (-not $SkipPlugins) {
        $codex = Get-Command codex -ErrorAction SilentlyContinue
        if (-not $codex) {
            $binRoot = Join-Path $env:LOCALAPPDATA "OpenAI\Codex\bin"
            if (Test-Path -LiteralPath $binRoot) {
                $candidate = Get-ChildItem -LiteralPath $binRoot -Recurse -Filter codex.exe -File |
                    Sort-Object FullName -Descending |
                    Select-Object -First 1
                if ($candidate) {
                    $codex = $candidate.FullName
                }
            }
        }

        if ($codex) {
            $codexPath = if ($codex -is [System.Management.Automation.CommandInfo]) {
                $codex.Source
            } else {
                $codex
            }
            Write-Host "`nRestoring Codex plugins (best effort)"
            foreach ($plugin in $manifest.plugins) {
                & $codexPath plugin add $plugin.selector --json
                if ($LASTEXITCODE -eq 0) {
                    Write-Host "  INSTALLED $($plugin.selector)"
                } else {
                    Write-Warning "Plugin restore failed: $($plugin.selector)"
                }
            }
        } else {
            Write-Warning "Plugin restore skipped: codex CLI was not found."
        }
    }

    Write-Host "`nRestart Codex to load the installed skills."
} finally {
    if (Test-Path -LiteralPath $tempRoot) {
        $resolvedTemp = [System.IO.Path]::GetFullPath($tempRoot)
        $systemTemp = [System.IO.Path]::GetFullPath([System.IO.Path]::GetTempPath())
        if ($resolvedTemp.StartsWith($systemTemp, [System.StringComparison]::OrdinalIgnoreCase)) {
            Remove-Item -LiteralPath $resolvedTemp -Recurse -Force
        }
    }
}
