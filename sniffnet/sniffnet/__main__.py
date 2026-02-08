from sniffnet.utils.banner.preview import init
from sniffnet.utils.argparser.parser import arg_parser

from sniffnet.utils.sniffer.sniff_packets import sniff_packets


def main():
    init()
    interface = arg_parser()

    sniff_packets(
        iface=interface
    )


if __name__ == '__main__':
    main()
