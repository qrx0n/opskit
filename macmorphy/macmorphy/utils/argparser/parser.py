from argparse import ArgumentParser


def parser():
    parser = ArgumentParser(
        prog='MAC Morphy',
        description='MAC Address Changer'
    )

    parser.add_argument(
        '-i', '--interface'
    )

    parser.add_argument(
        '-m', '--mac_addr'
    )

    parser.add_argument(
        '-r', '--random',
        action='store_true'
    )

    parser.add_argument(
        '-t', '--timeout'
    )

    return parser.parse_args()
