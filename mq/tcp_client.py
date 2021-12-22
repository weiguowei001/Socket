import socket
import utility


def tcp_client(server):
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc.connect(server)

    data = soc.recv(12)
    peer_addr = utility.bytes_to_addr(data[:6])
    my_addr = utility.bytes_to_addr(data[6:])

    if my_addr[0] == peer_addr[0]:
        local_addr = (soc.getsockname()[0], peer_addr[1])
        # ... connect to local address ...


server_addr = ('127.0.0.1', 4000)  # the server's  public address
tcp_client(server_addr)
