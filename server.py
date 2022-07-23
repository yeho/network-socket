import socket

SER_ADDR = input("ip:")
SER_PORT = int(input("Puerto:"))

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM )
server.bind((SER_ADDR, SER_PORT))
server.listen(1)
print("servidor iniciado... rock&roll baby!....")
connection, address = server.accept()
print("Se conecto un cliente...", address)
while 1:
    data = connection.recv(1024)
    if not data: break
    connection.sendall(b'--llego el mensaje al server--\n')
    print(data.decode('utf-8'))
connection.close()