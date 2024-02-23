import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 12345))

server.listen()

while True:
    client, addr = server.accept()
    print(f'Connection from {addr}')
    print(client.recv(1024).decode('utf-8')) 
    client.send("Hello, from server!".encode('utf-8'))
    print(client.recv(1024).decode('utf-8'))
    client.send("Bye, from server!".encode('utf-8'))
    client.close()