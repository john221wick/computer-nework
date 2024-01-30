import socket
import datetime

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1' 
port = 12345
server_socket.bind((host, port))
server_socket.listen(5)

print("Server is waiting for client request...")

conn, addr = server_socket.accept()
print(f"Connected to {addr}")

current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
conn.send(current_time.encode())

conn.close()