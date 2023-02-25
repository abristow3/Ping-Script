import os
import socket
import netifaces


def ping(url: str):
    print(os.system(f"ping -i 1 -c 25 {url}"))


def get_client_ip():
    hostname = socket.gethostname()
    print(f"Alex's Client IP: {socket.gethostbyname(hostname)}")


def get_subnet():
    address = netifaces.ifaddresses('en0')
    print(f"Alex's Subnet Mask: {address[netifaces.AF_INET][0]['netmask']}")


def get_default_gateway():
    gateway = netifaces.gateways()
    print(f"Alex's Default Gateway IP: {gateway['default'][netifaces.AF_INET][0]}")


if __name__ == '__main__':
    # Get the client host name and IP Address
    get_client_ip()

    # Get the default gateway IP Address
    get_default_gateway()

    # Get the Subnet Mask
    get_subnet()

    # Ping Amazon.com 25 times
    amazon_url = "www.amazon.com"
    ping(amazon_url)
