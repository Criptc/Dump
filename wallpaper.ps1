Set-ItemProperty -path 'HKCU:\Control Panel\Desktop\' -name wallpaper -value C:\Users\$env:UserName\AppData\Local\Temp\img.jpg
rundll32.exe user32.dll, UpdatePerUserSystemParameters
