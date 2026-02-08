from time import strftime

from config.colors import COLORS
from scapy.all import Ether, DHCP


def collect(packet):
    host, mac, id_, ip = [None] * 4

    if packet.haslayer(Ether):
        mac = packet.getlayer(Ether).src


    for item in packet[DHCP].options:
        try: 
            label, value = item

        except ValueError:
            continue

        
        if label == 'hostname':
            host = value.decode()

        elif label == 'requested_addr':
            ip = value

        elif label == 'vendor_class_id':
            id_ = value.decode()


    if host and mac and id_ and ip:
        print(
            f"{COLORS['RESET']}[ {COLORS['DATE']}{strftime('%Y-%m-%d - %H:%M:%S')}{COLORS['RESET']} ] : {COLORS['DATA']}{host}{COLORS['RESET']} / {COLORS['DATA']}{id_} {COLORS['RESET']}| {COLORS['DATA']}{mac} {COLORS['RESET']}| {COLORS['DATA']}{ip} {COLORS['RESET']}"
        )
