from scapy.all import IP


def ip(addr):
    return IP(
        dst=addr
    )
