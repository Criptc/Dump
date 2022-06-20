import zlib
import shutil
from os import rename
import os
from time import sleep

def compress():
    # get file to compress
    inp = input('file to compress: ')
    f = open(inp, 'rb')
    Bytes = f.read() # get bytes of the file
    f.close()
    #-----add file extention to the end of the bytes-----#
    if inp.endswith('.exe'):
        filetype = [0xFF]
        filename = inp.replace('.exe', '')
    elif inp.endswith('.py'):
        filetype = [0xFE]
        filename = inp.replace('.py', '')
    elif inp.endswith('.txt'):
        filetype = [0xFD]
        filename = inp.replace('.txt', '')
    elif inp.endswith('.bat') or inp.endswith('.cmd'):
        filetype = [0xFC]
        filename = inp.replace('.bat', '')
    elif inp.endswith('.png'):
        filetype = [0xFB]
        filename = inp.replace('.png', '')
    elif inp.endswith('.jpeg') or inp.endswith('.jpg'):
        filetype = [0xFA]
        filename = inp.replace('.jpg')
    elif inp.endswith('.pdf'):
        filetype = [0xF9]
        filename = inp.replace('.pdf')
    elif inp.endswith('.bin'):
        filetype = [0xF8]
        filename = inp.replace('.bin')
    else:
        raise Exception('unknown file extention')
    #-----add file extention to the end of the bytes-----#
    Bytes = zlib.compress(Bytes) + bytearray(filetype) # combind the bytes compressed and the filetype bytes
    f = open(inp, 'wb')
    f.write(Bytes) # write the compressed bytes to the file
    f.close()
    zipedname = shutil.make_archive(filename, 'zip') # zip the file
    sleep(0.5)
    os.rename(zipedname, filename + '.ecf') #rename the file

def decompress():
    inp = input('file to decompress: ')
    if not inp.endswith('.ecf'):
        raise Exception('Can\'t decompress non .ecf filetype')
    f = open(inp, 'rb')
    Bytes = f.read()
    f.close()
    filetype = Bytes[-1:]
    Bytes = Bytes[:len(Bytes) - 1]
    Data = zlib.decompress(Bytes)
    if filetype == b'\xff':
        filetype = '.exe'
    elif filetype == b'\xfe':
        filetype = '.py'
    elif filetype == b'\xfd':
        filetype = '.txt'
    elif filetype == b'\xfc':
        filetype = '.bat'
    elif filetype == b'\xfb':
        filetype = '.png'
    elif filetype == b'\xfa':
        filetype = '.jpg'
    elif filetype == b'\xf9':
        filetype = '.pdf'
    elif filetype == b'\xf8':
        filetype = '.bin'
    else:
        filetype = '.txt'
    f = open(inp, 'wb')
    f.write(Data)
    f.close()
    filename = inp.replace('.ecf', '')  + filetype
    os.rename(inp, filename)

inp = input('compress or decompress: ')
inp = inp.lower()
if inp == 'compress' or inp == 'c':
    compress()
elif inp == 'decompress' or inp == 'd':
    decompress()