from linkforge.utils.crawl import crawl
from linkforge.utils.links import links
from linkforge.utils.valid import valid

from linkforge.banner.preview import init
from linkforge.config.colors import COLORS

from linkforge.argparser.parser import parser


def main():
    total = 0

    args = parser()

    url = args.url

    init()

    print(
        f"Extracted Links : {COLORS['RESET']}"
    )

    length_ = crawl(
        url
    )

    print("\n")

    print(
        f'{COLORS["RESET"]}INFO :'
    )

    print(
        f" [1]: {COLORS['INFO']}[!] Internal Links: {length_[0]}{COLORS['RESET']}"
    )
    print(
        f" [2]: {COLORS['INFO']}[!] External Links: {length_[1]}{COLORS['RESET']}"
    )
    print(
        f" [3]: {COLORS['INFO']}[!] Total Links: {length_[0] + length_[1]}{COLORS['RESET']}"
    )


if __name__ == '__main__':
    main()
