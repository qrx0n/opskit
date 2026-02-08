from os import system
from netfilterqueue import NetfilterQueue

from spoon.packets.process import process_packet


def main():
    QUEUE_NUM = 0

    system(
        f"iptables -I FORWARD -J NFQUEUE --queue-num {QUEUE_NUM}"
    )

    queue = NetfilterQueue()

    try:
        queue.bind(
            QUEUE_NUM, process_packet
        )
        queue.run()

    except KeyboardInterrupt:
        system(
            "iptables --flush
        )
