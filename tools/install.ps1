<#
.SYNOPSIS
  Instala a tradução pt-BR de Esoteric Ebb.
.PARAMETER GamePath
  Pasta do jogo (a que contém "Esoteric Ebb_Data"). Se omitido, tenta achar na Steam.
#>
param([string]$GamePath)

$ErrorActionPreference = 'Stop'

if (-not $GamePath) {
    $candidates = @(
        "${env:ProgramFiles(x86)}\Steam\steamapps\common\Esoteric Ebb",
        "$env:ProgramFiles\Steam\steamapps\common\Esoteric Ebb"
    )
    foreach ($d in 'C','D','E','F','G') {
        $candidates += "${d}:\Steam\steamapps\common\Esoteric Ebb"
        $candidates += "${d}:\SteamLibrary\steamapps\common\Esoteric Ebb"
    }
    $GamePath = $candidates | Where-Object { Test-Path "$_\Esoteric Ebb_Data" } | Select-Object -First 1
}
if (-not $GamePath -or -not (Test-Path "$GamePath\Esoteric Ebb_Data")) {
    Write-Error 'Jogo não encontrado. Rode: .\tools\install.ps1 -GamePath "C:\...\Esoteric Ebb"'
}

$loc = Join-Path $GamePath 'Esoteric Ebb_Data\StreamingAssets\Localization'
if (-not (Test-Path "$loc\Official")) {
    Write-Error "Pasta Localization/Official não encontrada em $loc (versão do jogo sem suporte a idiomas da comunidade?)."
}

$src = Join-Path $PSScriptRoot '..\PortugueseBR'
$dst = Join-Path $loc 'PortugueseBR'
New-Item -ItemType Directory -Force -Path $dst | Out-Null
Copy-Item "$src\*.csv" $dst -Force
Write-Host "Instalado em: $dst"
Write-Host 'Abra o jogo e escolha "Português (BR)" em Settings. Com o jogo aberto, Ctrl+R recarrega os CSVs.'
