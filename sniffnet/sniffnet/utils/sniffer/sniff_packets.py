from scapy.all import sniff

from sniffnet.config.filters import FILTERS
from sniffnet.utils.sniffer.procced_packet import procced_packet


def sniff_packets(iface: str) -> None:
    if iface:
        sniff(filter=FILTERS[80], prn=procced_packet, iface=iface, store=False)

    else:
        sniff(filter=FILTERS[80], prn=procced_packet, store=True)
