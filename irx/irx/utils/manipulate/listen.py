from scapy.all import sniff
from irx.utils.packet.collect import collect

from config.colors import COLORS
from config.filters import FILTERS


def dhcp():
    print(
        f"{COLORS['INFO']}DHCP Listener Initialized :"
    )


    sniff(
        prn=collect,
        filter=FILTERS['DHCP']
    )
