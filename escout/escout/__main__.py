from escout.banner.preview import init
from escout.config.colors import COLORS

from escout.utils.collect import collect
from escout.utils.response import response

from escout.argparser.parser import parser


def main():
    args = parser()
    
    init()

    print(f"{COLORS['BANNER']}Collected Email Addresses:{COLORS['RESET']}")

    response_ = response(
        args.url
    )
    
    data = collect(
        response_
    )

    for index, email in enumerate(data):
        print(f"[{index+1}]: {COLORS['DATA']}{email}{COLORS['RESET']}")


if __name__ == '__main__':
    main()
