from argparse import ArgumentParser


def parser():
    parser_ = ArgumentParser(
        prog='arpie'
    )

    
    parser_.add_argument(
        '-i',
        '--iface'
    )


    return parser_.parse_args()
