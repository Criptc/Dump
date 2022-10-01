import socket
import requests

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostbyname(socket.gethostname())
print(host)
try:
    server.bind((host, 44445))
    server.listen()
    client, addr = server.accept()
    print(addr)
    while True:
        try:
            data = client.recv(1024)
            print(data, '\n', len(data), '\n')
            print(data.decode())

        except: break
except:
    print('exception occurred, closing server')
    server.close()
    exit(1)
