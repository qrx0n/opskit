from scapy.all import send


def packet(raw, tcp, ip):
    send(
        ip / tcp / raw,
        loop=1,
        verbose=0
    )
