import zlib
import shutil
from os import rename
import os
from time import sleep

def compress():
    
    file_types = {
    'exe': 0xFF,
    'py': 0xFE,
    'txt': 0xFD,
    'bat': 0xFC,
    'cmd': 0xFC,
    'png': 0xFB,
    'jpg': 0xFA,
    'pdf': 0xF9,
    'bin': 0xF8
    }
    
    # get file to compress
    inp = input('file to compress: ')
    
    f = open(inp, 'rb')
    Bytes = f.read() # get bytes of the file
    f.close()
    
    #add file extention to the end of the bytes
     ext = inp.split('.')[-1].lower()
    if ext in file_types:
        filetype = [file_types[ext]]
        filename = inp.replace(f'.{ext}', '')
    else:
        raise Exception('unknown file extention')

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