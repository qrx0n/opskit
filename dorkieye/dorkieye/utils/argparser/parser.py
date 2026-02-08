from argparse import ArgumentParser


def parser():
    parser = ArgumentParser(
        prog='dorkieye'
    )

    parser.add_argument(
        '-c',
        '--config'
    )
    

    args = parser.parse_args()

    return args
