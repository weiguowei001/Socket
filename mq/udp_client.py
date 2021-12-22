import socket
from threading import Thread
import utility


def udp_client(server):
    soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    soc.sendto(b'', server)
    data, _ = soc.recvfrom(6)
    peer = utility.bytes_to_addr(data)
    print('peer:', *peer)

    Thread(target=soc.sendto, args=(b'hello', peer)).start()
    data, addr = soc.recvfrom(1024)
    print('{}:{} says {}'.format(*addr, data))


server_addr = ('127.0.0.1', 4000)  # the server's  public address
udp_client(server_addr)
