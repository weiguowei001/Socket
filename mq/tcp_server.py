import socket
import utility


def tcp_server(addr):
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc.bind(addr)
    soc.listen()

    client_a, addr_a = soc.accept()
    client_b, addr_b = soc.accept()
    client_a.send(utility.addr_to_bytes(addr_b) +
                  utility.addr_to_bytes(addr_a))
    client_b.send(utility.addr_to_bytes(addr_a) +
                  utility.addr_to_bytes(addr_b))

addr = ('0.0.0.0', 4000)
tcp_server(addr)
