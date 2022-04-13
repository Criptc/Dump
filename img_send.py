import socket
import threading
import time
import os
import zlib
import datetime as G
from pathlib import Path
E=str; D=' '; F=int
def fulltime():B=G.datetime.now().date();C=E;B=C(B);B=B.replace('-','/');B=B+D;A=G.datetime.now().time();A=C(A);A=A[:8];H=F(A[:2])-17;A=A[2:];A=C(H)+A;I=B+A;return I
HOST = '0.0.0.0'
PORT = 55555
print('waiting for connection')
sender = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    sender.bind((HOST, PORT))
except:
    print(f'{fulltime()}  cant bind')
    sender.close()
sender.listen()

def lts(s):
	B=''
	for A in s:B+=A
	return B

def work():
    nil = 0
    client, address = sender.accept()
    for fo in address:
        if nil != 1:
            client_ip = fo
            nil = 1
        elif nil == 1:
            client_port = fo
    
    nickname = client_ip + ':' + str(client_port)
    client.send('connected'.encode('ascii'))
    print(client.recv(1024).decode('ascii'))
    client.send('askfile'.encode('ascii'))
    file_name = client.recv(1024).decode('ascii')
    file_type = file_name.split('.')[-1:]
    file_type = lts(file_type)
    file_path = os.path.abspath(file_name)
    print(f'{fulltime()}  client requested file "{file_path}"')
    if file_type == 'exe' or 'png' or 'jpg' or 'jpeg' or 'webm' or 'mp4' or 'mp3':
        try:
            f = open(file_name, 'rb')
            no_file = False
        except:
            no_file = True
    else:
        try:
            f = open(file_name, 'r')
            no_file = False
        except:
            no_file = True
    if no_file != True:
        data = f.read()
        f.close()
        client.send(f'typertypest {file_type}'.encode('ascii'))
        time.sleep(1)
        client.send(zlib.compress(data))
    else:
        client.send('file not found'.encode('ascii'))
    print(client.recv(1024).decode('ascii'))
work()
