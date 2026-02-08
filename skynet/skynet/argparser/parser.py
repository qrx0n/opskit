from argparse import ArgumentParser


def parser():
    parser = ArgumentParser(
        prog='skynet'
    )

    parser.add_argument(
        '-r',
        '--range'
    )

    return parser.parse_args()
