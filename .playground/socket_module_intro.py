import socket

HOSTS = [
    "www.google.com",
    "MacBookPro.mynet",
    "www.python.org",
    "nosuchname"
]

for host in HOSTS:
    try:
        name, aliases, addresses = socket.gethostbyname_ex(host)
        print(host)
        print(f"\tAliases: {aliases}")
        print(f"\tAddresses: {addresses}")
    except socket.error as e:
        print(f"{host}: {e}")
