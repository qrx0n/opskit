from argparse import ArgumentParser


def parser():
    parser_ = ArgumentParser(
        prog='synner'
    )


    parser_.add_argument(
        '-t',
        '--target'
    )

    parser_.add_argument(
        '-p',
        '--port'
    )

    
    return parser_.parse_args()
