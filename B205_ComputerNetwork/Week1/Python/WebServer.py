from socket import *
import sys  # In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM)

# Prepare a server socket
serverSocket.bind(('', 6787))  # Bind to port 6789 on all interfaces
serverSocket.listen(1)  # Listen for incoming connections

while True:
    # Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()  # Accept a new connection

    try:
        message = connectionSocket.recv(1024).decode()  # Receive the request
        filename = message.split()[1]  # Extract the requested filename
        f = open(filename[1:])  # Open the file, remove leading '/'
        outputdata = f.read()  # Read the entire content

        # Send HTTP header line
        connectionSocket.send('HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n'.encode())

        # Send the content of the requested file
        connectionSocket.send(outputdata.encode())

        connectionSocket.close()  # Close the connection

    except IOError:
        # Send 404 Not Found response
        response_header = 'HTTP/1.1 404 Not Found\r\n\r\n'
        response_body = '<html><body><h1>404 Not Found</h1></body></html>'
        connectionSocket.send(response_header.encode() + response_body.encode())
        connectionSocket.close()  # Close the client socket

serverSocket.close()
sys.exit()  # Terminate the program