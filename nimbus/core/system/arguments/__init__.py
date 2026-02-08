from argparse import ArgumentParser, Namespace


def parser() -> Namespace:
    _parser = ArgumentParser(
        description='Reverse DNS Lookup Tool (Nimbus)'
    )

    _parser.add_argument(
        'ip',
        help='IP to perform Reverse Lookup on'
    )

    _parser.add_argument(
        '-a', '--all',
        action='store_true',
        help='Print all Websites on the Server.'
    )

    _parser.add_argument(
        '-c', '--config',
        help='Path to the Config file'
    )

    return _parser.parse_args()
