from scapy.all import TCP, RandShort


def tcp(port):
    return TCP(
        sport=RandShort(),
        dport=port,
        flags='S'
    )
