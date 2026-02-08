from scapy.all import Raw


def raw():
    return Raw(
        b'X' * 1024
    )
