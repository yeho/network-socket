import socket

SER_ADDR = input("ip: ")
SER_PORT = int(input("Puerto: "))

my_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM )
my_sock.connect((SER_ADDR, SER_PORT))
print("Conectado baby")

message = input("Mensaje a enviar: ")
my_sock.sendall(message.encode())
my_sock.close()