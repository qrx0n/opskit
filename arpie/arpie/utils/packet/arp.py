from scapy.all import sniff
from arpie.utils.packet.process import process


def sniffer(iface):
    sniff(
        store=False,
        prn=process,
        iface=iface
    )
