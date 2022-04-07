import threading
import socket

HOST = '0.0.0.0'
PORT = 55555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen

clients = []
nicknames = []

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
        client.send(message.encode('ascii'))

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            print(f'{nicknames[clients.index(client)]} says {message}')
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            nicknames.remove(nickname)
            break

def receive():
    while True:
        client, address = server.accept()
        print(f'client {str(address)} connected')
        
        client.send('NICK'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        
        nicknames.append(nickname)
        clients.append(client)
        
        print(f'nickname of {client} is {nickname}')
        broadcast(f'{nickname} joined the chat\n')
        client.send(f'connected to {HOST}:{PORT}')
        
        thread = threading.Thread(target=handel, args=(client,))
        thread.start()

print(f'{fulltime()}  server started at {HOST}:{PORT}')
receive()