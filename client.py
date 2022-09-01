import socket, threading, zlib, rsa

nickname = input('Nickname: ')
encrypt = False
key = ''
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('192.168.56.1', 55556))

def receive():
    while True:
        global encrypt
        try:
            if not encrypt:
                message = zlib.decompress(client.recv(4096)).decode()
                if message == 'NICK':
                    client.send(zlib.compress(nickname.encode()))
                if message == 'KEY':
                    key = zlib.decompress(client.recv(4096)).decode()
                    encrypt = True
                else:
                    print(message)
            else:
                message = zlib.decompress(rsa.decrypt(client.recv(4096), key)).decode()
                print(message)
        except Exception as Err:
            print('An error occurred')
            print(Err)
            client.close()
            break

def write():
    while True:
        global encrypt
        if not encrypt:
            message = f'{nickname}: {input()}'
            client.send(zlib.compress(message.encode()))
        else:
            message = f'{nickname}: {input()}'
            client.send(zlib.compress(rsa.encrypt(message.encode())))

recv = threading.Thread(target=receive)
wrt = threading.Thread(target=write)
recv.start()
wrt.start()