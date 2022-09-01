import socket, threading, zlib, datetime, re, rsa

host = socket.gethostbyname(socket.gethostname())
port = 55556

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients=[]
nicknames=[]
public_keys=[]
privet_keys=[]

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
        index = clients.index(client)
        priv_key = privet_keys[index]
        message = zlib.compress(rsa.encrypt(message, priv_key))
        client.send(message)

def handle(client):
    while True:
        try:
            index = clients.index(client) 
            message = client.recv(4096)
            message_useable = zlib.decompress(rsa.decrypt(message, privet_keys[index])).decode()
            print(f'{fulltime()} {message_useable}')
            message_useable = re.sub('.*:\s', '', message_useable)
            if message_useable.startswith('/'):
                if message_useable == '/help':
                    client.send(zlib.compress(rsa.encrypt(f'/help: this prompt \n/list: the people currently in the chat server\n'.encode(), privet_keys[index])))
                elif message_useable == '/list':
                    client.send(zlib.compress(rsa.encrypt(f'{nicknames}'.encode(), privet_keys[index])))
                else:
                    client.send(zlib.compress(rsa.encrypt(f'unkown command, {message_useable}'.encode(), privet_keys[index])))
            else:
                message = zlib.decompress(rsa.decrypt(message, privet_keys[index]))
                broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            pub_key = public_keys[index]
            public_keys.remove(pub_key)
            priv_key = privet_keys[index]
            privet_keys.remove(priv_key)
            nickname = nicknames[index]
            broadcast(f'{nickname} left the chat'.encode())
            print(f'{fulltime()} {nickname} left')
            nicknames.remove(nickname)
            break

def receive():
    while True:
        pub_key, priv_key = rsa.newkeys(1024)
        client, address = server.accept()
        print(f'{fulltime()} {str(address)} connected')
        client.send(zlib.compress('NICK'.encode()))
        nickname = zlib.decompress(client.recv(4096)).decode()
        client.send(zlib.compress('KEY'.encode()))
        client.send(zlib.compress(str(pub_key).encode()))
        nicknames.append(nickname)
        clients.append(client)
        privet_keys.append(priv_key)
        public_keys.append(pub_key)
        print(f'{fulltime()} Nickname of client is {nickname}')
        broadcast(zlib.compress(f'{nickname} joined the chat'.encode()))
        client.send(zlib.compress(rsa.encrypt('Connected to server'.encode(), priv_key)))

        t = threading.Thread(target=handle, args=(client,))
        t.start()

print('server started')
receive()
