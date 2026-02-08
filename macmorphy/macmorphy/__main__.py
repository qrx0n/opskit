from sys import exit
from time import sleep

from macmorphy.config.colors import COLORS

from macmorphy.utils.banner.preview import init

from macmorphy.utils.argparser.parser import parser
from macmorphy.utils.argparser.check import check_args

from macmorphy.utils.spoofer.manipulate import change
from macmorphy.utils.spoofer.init import random, current


def main():
    args = parser()
    config = check_args(args)

    init()

    if config['random']:
        while True:
            try:
                new = random()
                old = current(
                    config['interface']
                )

                change(
                    config['interface'],
                    new
                )

                print(f"{COLORS['OLD']}old [*] : {old.lower()}  {COLORS['SEPERATE']}|  {COLORS['NEW']}new [+] : {new.lower()}{COLORS['RESET']}")
                sleep(config['timeout'])

            except KeyboardInterrupt:
                exit()

    
    elif config['mac_addr']:
        old = current(
            config['interface']
        )

        change(
            config['interface'],
            args.mac_addr
        )
        
        print(f"{COLORS['OLD']}old : {old.lower()}  {COLORS['SEPERATE']}|  new : {COLORS['NEW']}{args.mac_addr.lower()}{COLORS['RESET']}")


if __name__ == '__main__':
    main()
