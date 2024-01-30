# RDT 3.0 Implementation README

## Overview
This is a basic implementation of the RDT (Reliable Data Transfer) 3.0 protocol using Python's socket programming. The code demonstrates reliable transmission of data over a network with packet loss simulation.

## Features
- **UDP Protocol:** Uses UDP sockets for data transmission.
- **Timeout Mechanism:** Implements timeouts for ACKs (Acknowledgements).
- **Packet Loss Simulation:** Randomly simulates packet loss to test reliability.

## Components
1. **Client:** Sends messages with sequence numbers and handles ACKs.
2. **Server:** Receives messages, sends ACKs, and simulates packet loss.

## How It Works
1. **Client sends messages** within a window size.
2. **Server receives messages** and randomly decides whether to acknowledge them or simulate packet loss.
3. **Client handles ACKs** and resends messages if timeout occurs.

## Requirements
- Python 3
- Socket library (standard in Python)

## Usage
1. **Run Server:** Execute the server script to start listening for messages.
2. **Run Client:** Execute the client script to start sending messages.

## Testing
- Observe the console output to see the packet transfer, ACK reception, and packet loss simulation.

## Note
- The client and server are set to communicate over `localhost` on port `12345`.