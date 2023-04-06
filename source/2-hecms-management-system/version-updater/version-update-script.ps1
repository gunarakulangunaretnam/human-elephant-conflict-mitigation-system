# Check if a version argument was provided
if ($args.Count -ne 1) {
    Write-Host "Error: Please provide a version number as an argument." -ForegroundColor Red
    exit 1
}

# Get the version number from the argument
$NewVersion = $args[0]

# Update the version number in the config file
(Get-Content config/app.php) | Foreach-Object {$_ -replace "'version' => '[^']*'", "'version' => '$NewVersion'"} | Set-Content config/app.php
