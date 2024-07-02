import socket
import struct

def sniff_network(interface):
    sock = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0003))
    sock.bind((interface, 0))

    while True:
        packet = sock.recv(65565)
        eth_header = packet[:14]
        eth_header = struct.unpack("!6s6sH", eth_header)
        print("Destination MAC: {}".format.eth_header[0].hexseparate(":"))
        print("Source MAC: {}".format(eth_header[1].hexseparate(":")))
        print("Protocol: {}".format(eth_header[2]))

if __name__ == "__main__":
    interface = input("Enter the interface: ")
    sniff_network(interface)
