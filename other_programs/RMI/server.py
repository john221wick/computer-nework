import socket
import json

def square(num):
    return num * num

host = '127.0.0.1'
port = 50001

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(1)
print("Server Started!")

conn, address = server_socket.accept()
print("Connection from:", address)

data = conn.recv(1024).decode()
request = json.loads(data)

if request["function"] == "square":
    result = square(request["args"][0])
    response = {"result": result}
else:
    response = {"error": "Unknown function"}

conn.send(json.dumps(response).encode())
conn.close()

