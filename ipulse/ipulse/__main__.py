from config.config import read_config

from ipulse.banner.preview import init

from ipulse.config.colors import COLORS

from ipulse.utils.details import details
from ipulse.utils.handler import handler

from ipulse.argparser.parser import parser


def main():
    args = parser()

    token = read_config(args.config)


    _handler_ = handler(
        token=token
    )

    _details_ = details(
        handler=_handler_,
        ip=args.ip_addr
    )

    init()

    for field, value in _details_.all.items():
        print(f"{COLORS['FIELD']}{field.upper()} : {COLORS['VALUE']}{value}{COLORS['RESET']}")


if __name__ == '__main__':
    main()
