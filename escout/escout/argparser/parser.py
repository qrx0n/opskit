from argparse import ArgumentParser


def parser():
    parser = ArgumentParser(
        prog='escout'
    )

    parser.add_argument(
        '-u',
        '--url'
    )
    

    args = parser.parse_args()

    return args
