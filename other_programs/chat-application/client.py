import socket

server_name = 'localhost'
server_port = 12000
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_name, server_port))
print('Connected to the server.')

while True:
    message = input("Enter your message (type 'close' to exit): ")

    if message.lower() == "close":
        client_socket.close()
        break

    client_socket.send(message.encode())
    modified_message = client_socket.recv(2048)

    if not modified_message:
        print("server has closed the connection.")
        break

    print(f'message from server: {modified_message.decode()}')

client_socket.close()
print("disconnected from the server.")
