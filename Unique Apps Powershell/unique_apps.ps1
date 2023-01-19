# Created by   : Desmond Ho
# Date         : 2023-01-13

# Description   : script takes in the name of 2 computers (old and new) and returns a list / txt file of all apps that 
#  are on the old computer and not on the new computer

#  show custom error is parameters are not passed in

param (
     [string] $oldComputer = "null",
     [string] $newComputer = "null",
     [string] $outputFile = "null"
     )


#  show custom error if parameters are not passed in
if ($oldComputer -eq "null" -or $newComputer -eq "null" -or $outputFile -eq "null") {
    Write-Host "Please pass in the name of the old and new computer" -ForegroundColor Blue -BackgroundColor Blue
    Write-Host "Example: unique_apps.ps1 -oldComputer oldComputerName -newComputer newComputerName -outputFile [ txt | csv | console]" -ForegroundColor Red
    Write-Host "Or: unique_apps.ps1 oldComputerName newComputerName [ txt | csv | console] " -ForegroundColor Red
    exit
}

# Its working trust me
Write-Host "Searching...."

# get all apps installed on old computer
try {
    $oldApps = Get-WmiObject -ComputerName $oldComputer -Class Win32_Product | Select-Object -Property Name, Version | Where-Object {$_.Name -notlike "*Microsoft*" -and $_.Name -notlike "*Windows*" -and $_.Name -notlike "*Citrix*" -and $_.Name -notlike "*Intel*"}

} catch {
    Write-Host "Error: Old Computer Name is not valid" -ForegroundColor Red
    exit
} 

# get all apps installed on new computer
try {
    $newApps = Get-WmiObject -ComputerName $newComputer -Class Win32_Product | Select-Object -Property Name, Version | Where-Object {$_.Name -notlike "*Microsoft*" -and $_.Name -notlike "*Windows*" -and $_.Name -notlike "*Citrix*" -and $_.Name -notlike "*Intel*"}

} catch {
    Write-Host "Error: New Computer Name is not valid" -ForegroundColor Red
    exit
}

# line

write-host "------------------------------------"

#  both objects located, get length of each
$oldAppsLength = $oldApps.Length
$newAppsLength = $newApps.Length

write-Host "$oldAppsLength programs found on old computer" -ForegroundColor Yellow

write-Host "$newAppsLength programs found on new computer"  -ForegroundColor Yellow

# line

write-host "------------------------------------"


# get a list of all unique apps on old computer that is not on new computer

# empty list to store unique apps
$uniqueApps = @()

foreach ($oldApp in $oldApps) {
    
    if ($oldApp.Name -notin $newApps) {
        $uniqueApps += $oldApp.Name
    }
    
}

# success! 

write-host $uniqueApps.Count "Unique Apps Found" -ForegroundColor Green

# line

write-host "------------------------------------"

# if output file is specified, write to file
if ($outputFile -eq "csv" -or $outputFile -eq "CSV") {
    $uniqueApps | Out-File $oldComputer"_unique_apps.csv" -Encoding UTF8
    write-host "Unique Apps written to" $oldComputer"_unique_apps.csv" -ForegroundColor Green
} 

elseif ($outputFile -eq "txt" -or $outputFile -eq "TXT") {
    $uniqueApps | Out-File $oldComputer"_unique_apps.txt" -Encoding UTF8
    write-host "Unique Apps written to" $oldComputer"_unique_apps.txt" -ForegroundColor Green
} 

elseif ($outputFile -eq "console" -or $outputFile -eq "CONSOLE") {
    write-host "Unique Apps written to console" -ForegroundColor Green
} 

else {
    write-host "No output file specified" -ForegroundColor Yellow
}


# 2. get all apps installed on computer
# $apps = Get-WmiObject -Class Win32_Product -ComputerName $computer

# 3. print all apps to screen

# foreach ($app in $apps) {
#     Write-Host $app.Name
# }

# poggers
Write-Host "Script Created by Desmond Ho, Ph.D, Msc, TCP, UDP, LLC" -BackgroundColor Blue -ForegroundColor White

# Path: unique_apps.ps1



