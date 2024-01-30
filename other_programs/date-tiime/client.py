import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'  # Server's address
port = 12345

client_socket.connect((host, port))

data = client_socket.recv(1024)
print(f"Date and Time from Server: {data.decode()}")

client_socket.close()


