import socket
from threading import Thread


import socket
import struct

def addr_to_bytes(addr):
    return socket.inet_aton(addr[0]) + struct.pack('H', addr[1])

def bytes_to_addr(addr):
    return (socket.inet_ntoa(addr[:4]), struct.unpack('H', addr[4:])[0])

def udp_client(server):
    soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    soc.sendto(b'', server)
    data, _ = soc.recvfrom(6)
    peer = bytes_to_addr(data)
    print('peer:', *peer)

    Thread(target=soc.sendto, args=(b'hello', peer)).start()
    data, addr = soc.recvfrom(1024)
    print('{}:{} says {}'.format(*addr, data))

server_addr = ('127.0.0.1', 4000) # the server's  public address
udp_client(server_addr)