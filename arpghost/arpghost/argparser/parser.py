from argparse import ArgumentParser


def parser():
    parser = ArgumentParser(
        prog='arpghost'
    )

    parser.add_argument(
        '-t',
        '--target'
    )

    parser.add_argument(
        '-H',
        '--host'
    )

    parser.add_argument(
        '-v',
        '--verbose',
        action="store_true"
    )
    
    
    return parser.parse_args()
