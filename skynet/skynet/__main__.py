from skynet.banner.preview import init

from skynet.utils.result import result
from skynet.utils.clients import clients

from skynet.argparser.parser import parser

from skynet.config.colors import COLORS
from skynet.config.messages import MESSAGES


def main():
    args = parser()

    init()

    print(f"{COLORS['BANNER']}{MESSAGES['startup']}{COLORS['RESET']}\n")

    result_ = result(
        range=args.range
    )

    clients_ = clients(
        result=result_
    )

    for index, client in enumerate(clients_):
        print(f"[{index+1}]: {COLORS['TABLE']}{client['ip']} -> {client['mac']}{COLORS['RESET']}")


if __name__ == '__main__':
    main()
