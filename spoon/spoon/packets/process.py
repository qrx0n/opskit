from scapy.all import DNSRR, IP

from spoon.config.dev import dns_hosts
from spoon.packets.modify import modify_packet


def process_packet(packet):
    scapy_packet = IP(
        packet.get_payload()
    )

    if (scapy_packet.haslayer(DNSRR)):
        print(
            f"[Before] : {scapy_packet.summary()}"
        )

        try:
            scapy_packet = modify_packet(
                scapy_packet, dns_hosts
            )

        except IndexError:
            pass

        print(
            f"[After] : {scapy_packet.summary()}"
        )

        packet.set_payload(
            bytes(scapy_packet)
        )

        packet.accept()

