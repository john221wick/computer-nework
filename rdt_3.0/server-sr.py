import socket
import random


server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('localhost', 12345))

expected_seq_num = 0
while True:
    message, address = server_socket.recvfrom(1024)
    seq_num = int(message.decode())


    if random.random() > 0.2:  # 20% packets are lost randomly
        print(f"Packet with sequence number {seq_num} received.")
        if seq_num == expected_seq_num:
            print(f"Acknowledging {seq_num}")
            server_socket.sendto(str(seq_num).encode(), address)
            expected_seq_num += 1
    else:
        print(f"Packet loss, sequence number {seq_num}")
