from argparse import ArgumentParser


def parser():
    parser = ArgumentParser(
        prog='ipulse'
    )

    parser.add_argument(
        '-a',
        '--ip_addr'
    )

    parser.add_argument(
        '-c',
        '--config'
    )
    

    args = parser.parse_args()

    return args
