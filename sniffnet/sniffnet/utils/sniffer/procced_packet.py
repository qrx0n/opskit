from scapy.all import IP, Raw
from scapy.layers.http import HTTPRequest

from sniffnet.config.colors import COLORS


def procced_packet(packet):
    if packet.haslayer(HTTPRequest):
        url = packet[HTTPRequest].Host.decode() \
            + packet[HTTPRequest].Path.decode()
        
        ip = packet[IP].src

        method = packet[HTTPRequest].Method.decode()

        print(f"{COLORS['PACKET']}[*] {ip} : requested {url} with {method}{COLORS['RESET']}")


        if packet.haslayer(Raw) and method == 'POST':
            print(f"\n{COLORS['RAW']}[!] Some useful RAW data : {packet[Raw].load}{COLORS['RESET']}\n")
