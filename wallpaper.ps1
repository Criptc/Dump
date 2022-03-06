Set-ItemProperty -path 'HCU:\Control Panel\Desktop\' -name wallpaper -value $1
rundll32.exe user32.dll, UpdatePerUserSystemParameters