from arpie.banner.banner import init
from arpie.argparser.parser import parser

from arpie.utils.packet.arp import sniffer


def main():
    args = parser()

    init()

    sniffer(
        args.iface
    )


if __name__ == '__main__':
    main()
