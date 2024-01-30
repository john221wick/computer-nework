import socket
import time
import random


client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.settimeout(2.0)  # Setting a timeout for acks


base = 0
next_seq_num = 0
window_size = 4  
messages = ['Message 1', 'Message 2', 'Message 3', 'Message 4', 'Message 5', 'Message 6']

def send_message(seq_num):
    message = f"{seq_num}"
    print(f"Sending packet with sequence number {seq_num}")
    client_socket.sendto(message.encode(), ('localhost', 12345))

# start sending messages
while base < len(messages):
    while next_seq_num < base + window_size and next_seq_num < len(messages):
        send_message(next_seq_num)
        next_seq_num += 1

# wait for ack or timeout
    try:
        ack, _ = client_socket.recvfrom(1024)
        ack = int(ack.decode())
        print(f"Acknowledged for sequence number {ack}")
        base = ack + 1
    except socket.timeout:
        print("Timeout occurred, resending from sequence number:", base)
        next_seq_num = base  # Resetting next_seq_num to resend the packets

client_socket.close()
