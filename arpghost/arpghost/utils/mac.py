from scapy.all import Ether, ARP, srp


def get(ip):
    ans, _ = srp(
        Ether(
            dst='ff:ff:ff:ff:ff:ff'
        ) / ARP(
            pdst=ip
        ),
        timeout=3,
        verbose=0
    )


    if ans:
        return ans[0][1].src
