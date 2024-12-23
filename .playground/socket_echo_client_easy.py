import socket
from collections import namedtuple
from typing import Dict


def get_constants(prefix: str) -> Dict[str, str]:
    """
    Create a dictionary mapping socket module constants to their names
    """
    return {getattr(socket, n): n for n in dir(socket) if n.startswith(prefix)}


families = get_constants("AF_")
types = get_constants("SOCK_")
protocols = get_constants("IPPROTO_")


# the create_connection() function takes in a server address and derives the best address to use for the connection and what type of socket to use
# this makes it easy to connect to the server
ServerAddress = namedtuple("ServerAddress", ["address", "port"])
server_address = ServerAddress(address="localhost", port=10_000)
print(f"connecting to {server_address.address} port {server_address.port}")
client_socket = socket.create_connection(server_address)

# print information about the connection created by the "create_connection()" function
print(f"Family: {families[client_socket.family]}")
print(f"Type: {types[client_socket.type]}")
print(f"Protocol: {protocols[client_socket.proto]}")
print()

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
