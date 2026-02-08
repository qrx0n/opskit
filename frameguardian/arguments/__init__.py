from argparse import ArgumentParser


def parser() -> ArgumentParser:
    _parser = ArgumentParser(
        description='Clickjacking Vulnerability Scanner (FrameGuardian)'
    )

    _parser.add_argument(
        'uri',
        type=str,
        help='The URI of the Website to Check'
    )

    _parser.add_argument(
        '-l', '--log',
        action='store_true',
        help='Print out the Response Headers'
    )

    return _parser.parse_args()
