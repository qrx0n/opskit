from scapy.all import ARP
from arpie.utils.network.mac import get

from config.colors import COLORS


def process(packet):
    if packet.haslayer(ARP):
        if packet[ARP].op == 2:
            try:
                mac = get(
                    packet[ARP].psrc
                )

                response = packet[ARP].hwsrc

                if mac != response:
                    print(
                        f"{COLORS['RESET']}[!] {COLORS['INFO']}You are under attack, MAC : {mac}; RESPONSE: {response}"
                    )
            
            except IndexError:
                pass
