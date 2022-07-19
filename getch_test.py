from getch import _Getch
getch = _Getch()
from time import sleep

while True:
    sleep(0.2)
    key = ord(getch())
    print(key)


