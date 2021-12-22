import socket
import utility


def udp_server(addr):
    soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    soc.bind(addr)

    _, client_a = soc.recvfrom(0)
    _, client_b = soc.recvfrom(0)
    soc.sendto(utility.addr_to_bytes(client_b), client_a)
    soc.sendto(utility.addr_to_bytes(client_a), client_b)


addr = ('0.0.0.0', 4000)
udp_server(addr)
