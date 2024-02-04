# Remote Method Invocation (RMI) Example

This example demonstrates a basic Remote Method Invocation (RMI) setup using Python's socket programming. RMI allows a program to execute a method on a remote server as if it were a local call. This particular example includes a server and a client script that communicate over a network to perform square operations on numbers.

## Server

The server script sets up a socket listener on a specified port. It waits for a connection from a client, receives a JSON request containing a function name and arguments, processes the request, and sends back a JSON response with the result. Currently, it supports a single function, `square`, which squares the provided number.

### Setup and Execution

1. Ensure Python is installed on your system.
2. Save the server code to a file, for example, `server.py`.
3. Run the server script using Python:

```bash
python server.py
```

The server will start and print "Server Started!" to indicate it is listening for connections.

## Client

The client script connects to the server using the server's IP address and port. It sends a JSON request to the server asking to execute the `square` function with a specified argument. After sending the request, it waits for a response from the server, receives the JSON response containing the result, prints it, and then closes the connection.

### Setup and Execution

1. Ensure the server script is running and listening for connections.
2. Save the client code to a file, for example, `client.py`.
3. Run the client script using Python, ensuring it is configured to connect to the correct server IP and port:

```bash
python client.py
```

The client will connect to the server, send the request, and print the response received from the server.

## Important Notes

- This example uses localhost (`127.0.0.1`) and port `50001` for demonstration purposes. For actual use, replace these with the server's IP address and port.
- The code demonstrates basic socket communication and JSON handling in Python. It does not include error handling, authentication, or encryption, which are essential for production environments.
- Always ensure your network configurations allow for the intended connections and that you implement proper security measures when deploying networked applications.

This RMI example is a simple demonstration of how client-server communication can be implemented in Python for remote method invocations. It can be extended to support more complex operations, multiple functions, and enhanced security features.