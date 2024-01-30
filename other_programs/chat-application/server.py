import socket

server_port = 12000
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('', server_port))
server_socket.listen(1)
print(f'server is ready to receive on port {server_port}.')

while True:
    connection_socket, addr = server_socket.accept()
    print(f'connected to client: {addr}')

    while True:
        message = connection_socket.recv(2048)
        if not message:
            print(f"connection with {addr} closed.")
            break

        modified_message = message.decode().upper()
        connection_socket.send(modified_message.encode())

    connection_socket.close()
