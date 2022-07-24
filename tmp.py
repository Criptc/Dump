import zlib

with open ('ccc2_install.exe.png', 'wb+') as f:
    for chunk in iter(lambda: f.read(4096), b""):
        f.write(zlib.decompress(chunk))

