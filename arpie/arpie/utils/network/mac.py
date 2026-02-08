from scapy.all import Ether, ARP, srp


def get(ip):
    packet = Ether(
        dst='ff:ff:ff:ff:ff:ff'
    ) / ARP(
        pdst=ip
    )

    return srp(
        packet,
        timeout=3,
        verbose=False
    )[0][0][1].hwsrc
