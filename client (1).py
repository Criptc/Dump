import socket, threading, zlib

nickname = input('Nickname: ')

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('192.168.56.1', 55556))

def receive():
    while True:
        try:
            message = zlib.decompress(client.recv(4096)).decode()
            if message == 'NICK':
                client.send(zlib.compress(nickname.encode()))
            else:
                print(message)
        except Exception as Err:
            print('An error occurred')
            print(Err)
            client.close()
            break

def write():
    while True:
        message = f'{nickname}: {input()}'
        client.send(zlib.compress(message.encode()))

recv = threading.Thread(target=receive)
wrt = threading.Thread(target=write)
recv.start()
wrt.start()