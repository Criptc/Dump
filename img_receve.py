import socket
import threading
import datetime as G
import zlib
HOST = '0.0.0.0'; PORT = 55555; E=str; D=' '; F=int
def fulltime():B=G.datetime.now().date();C=E;B=C(B);B=B.replace('-','/');B=B+D;A=G.datetime.now().time();A=C(A);A=A[:8];H=F(A[:2])-17;A=A[2:];A=C(H)+A;I=B+A;return I
print('connecting')
recever = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    recever.connect((HOST, PORT))
except:
    print('couldnt connect')
    exit(1)
print(recever.recv(1024).decode('ascii'))

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(0)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

recever.send(f'{fulltime()}  connected to {get_ip()}'.encode('ascii'))

def lts(s):
	B=''
	for A in s:B+=A
	return B

def receve():
    while True:
        data = recever.recv(1024)
        try:
            data = data.decode('ascii')
        except:
            break
        if data != '':
            if data == 'prep':
                break
            elif 'typertypest' in data:
                data_list = data.split(' ')
                file_type = data_list[-1:]
            elif data == 'askfile':
                askfile()
            elif data == 'file not found':
                print('file not found')
            else:
                print(data)
    file_data = data
    try:
        print(file_data.decode('ascii'))
    except:
        data = zlib.decompress(data)
        full_file = 'temp.' + lts(file_type)
        if file_type == 'exe' or 'png' or 'jpg' or 'jpeg' or 'webm' or 'mp4' or 'mp3':
            f = open(full_file, 'x')
            f.close()
            f = open(full_file, 'wb')
            f.write(data)
        else:
            f = open(full_file, 'x')
            f = open(full_file, 'w')
            f.write(data)
        print(f'data writen to {full_file}')
        recever.send(f'{fulltime()}  file writen succesfuly'.encode('ascii'))
        f.close()
        recever.close()
        exit()
    receve()

def askfile():
    file = input('enter image or video name you want')
    if file != '':
        recever.send(file.encode('ascii'))
    else:
        print("can't ask for non named file")
receve()
