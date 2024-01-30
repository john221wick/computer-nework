import socket
import json

host = '127.0.0.1'
port = 50001

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))

request = {
    "function": "square",
    "args": [5]
}

client_socket.send(json.dumps(request).encode())
data = client_socket.recv(1024).decode()
response = json.loads(data)
print("Response from server:", response)

client_socket.close()

