import socket, threading, zlib, datetime, re

host = socket.gethostbyname(socket.gethostname())
port = 55556

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients=[]
nicknames=[]

def fulltime():
    tim = datetime.datetime.now().date()
    tim = str(tim)
    tim = tim.replace('-', '/')
    tim = tim + ' '
    time = datetime.datetime.now().time()
    time = str(time)
    time = time[:8]
    fulltime = tim + time
    return fulltime

def broadcast(message):
    for client in clients:
        client.send(message)

def handle(client):
    while True:
        try:
            index = clients.index(client) 
            message = client.recv(4096)
            message_useable = zlib.decompress(message).decode()
            print(f'{fulltime()} {message_useable}')
            message_useable = re.sub('.*:\s', '', message_useable)
            if message_useable.startswith('/'):
                if message_useable == '/help':
                    client.send(zlib.compress(f'/help: this prompt \n/list: the people currently in the chat server\n'.encode()))
                elif message_useable == '/list':
                    client.send(zlib.compress(f'{nicknames}'.encode()))
                else:
                    client.send(zlib.compress(f'unkown command, {message_useable}'))
            else:
                broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f'{nickname} left the chat'.encode())
            print(f'{fulltime()} {nickname} left')
            nicknames.remove(nickname)
            break

def receive():
    while True:
        client, address = server.accept()
        print(f'{fulltime()} {str(address)} connected')
        client.send(zlib.compress('NICK'.encode()))
        nickname = zlib.decompress(client.recv(4096)).decode()
        nicknames.append(nickname)
        clients.append(client)
        print(f'{fulltime()} Nickname of client is {nickname}')
        broadcast(zlib.compress(f'{nickname} joined the chat'.encode()))
        client.send(zlib.compress('Connected to server'.encode()))

        t = threading.Thread(target=handle, args=(client,))
        t.start()

print('server started')
receive()
