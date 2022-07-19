from getch import _Getch
getch = _Getch()

while True:
    key = ord(getch())
    if key == 27:
        exit(0)
    print(key)
