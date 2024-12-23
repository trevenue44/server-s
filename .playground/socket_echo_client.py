import socket
from collections import namedtuple

# create a TCP/IP socket
# - AF_NET to specify IPv4
# - SOCK_STREAM to specifies the type as a stream socket in order to use TCP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the socket to a port where a server is listening
ServerAddress = namedtuple("ServerAddress", ["address", "port"])
server_address = ServerAddress(address="localhost", port=10_000)
print(f"connecting to {server_address.address} port {server_address.port}")
client_socket.connect(server_address)

try:
    # send data
    message = b"This is the message. It'll be echo-ed."
    print(f"sending {message!r}")
    client_socket.sendall(message)

    # look for response
    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
        data = client_socket.recv(16)
        amount_received += len(data)
        print(f"received {data!r}")
finally:
    print("closing socket")
    client_socket.close()
