from scapy.all import ARP, Ether, srp

from skynet.config.config import PARAMS


def result(range: str):
    arp = ARP(
        pdst=range
    )

    ether = Ether(
        dst=PARAMS['dst']
    )

    packet = ether / arp


    return srp(
        packet,
        timeout=3,
        verbose=0
    )[0]
