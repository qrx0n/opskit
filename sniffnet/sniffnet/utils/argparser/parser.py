from argparse import ArgumentParser


def arg_parser():
    parser = ArgumentParser(
        prog='sniffnet',
        description='HTTP Packet Sniffer'
    )

    parser.add_argument(
        '-i',
        '--interface',
        help='interface to sniff'
    )

    args = parser.parse_args()
    
    return args.interface
