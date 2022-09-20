import socket
import sys


def send_message(message, ip, port):
    port = int(port)
    opened = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    byte_message = bytes(message, "utf-8")
    opened.sendto(byte_message,(ip,port))
    print(f'sent "{message}" to {ip}')

if __name__ == "__main__":
    send_message(sys.argv[1], sys.argv[2], sys.argv[3])