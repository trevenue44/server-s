import socket
from collections import namedtuple

# create a TCP/IP socket
# - AF_NET to specify IPv4
# - SOCK_STREAM to specifies the type as a stream socket in order to use TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind the socket to a server address
ServerAddress = namedtuple("ServerAddress", ["address", "port"])
server_address = ServerAddress(address="localhost", port=10_000)
print(f"starting up server on {server_address.address} and port {server_address.port}")
server_socket.bind(server_address)

# listen for incoming connections
# The backlog argument defines the maximum length to which the queue of pending connections for may grow
# (ref: https://stackoverflow.com/questions/48244322/listen-method-parameters-in-python)
server_socket.listen(1)

while True:

    # wait for a connection
    print("waiting for connection")
    connection, client_address = server_socket.accept()

    try:
        print(f"connection from {client_address}")

        # receive the data in small chunks and restransmit it to client
        while True:
            data = connection.recv(16)
            print(f"received {data!r}")

            if data:
                print("sending data back to client")
                connection.sendall(data)
            else:
                print(f"no data from {client_address}")
                break
    finally:
        # clean up the connection
        connection.close()
