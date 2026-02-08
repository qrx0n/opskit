from sys import exit
from colorama import Fore # type: ignore

from nimbus.core.dns import Lookup # type: ignore

from nimbus.core.system.config import Config # type: ignore
from nimbus.core.system.arguments import parser # type: ignore


def main():
    _parser = parser()

    _config = Config(
        _parser.config
    )

    _lookup = Lookup(
        _config._return(
            'viewdns',
            'api_key'
        )
    )

    if (not _lookup.valid(
        _parser.ip
    )):
        print(
            f"\n[ {Fore.RED}-{Fore.RESET} ] : {Fore.LIGHTRED_EX}Invalid IP Address{Fore.RESET} : '{Fore.CYAN}{_parser.ip}{Fore.RESET}';\n"
        )

        exit(
            1
        )

    domain = _lookup.lookup(
        _parser.ip
    )

    if domain:
        print(
            f"\n[ {Fore.GREEN}+{Fore.RESET} ] : {Fore.LIGHTGREEN_EX}IP{Fore.RESET} : '{Fore.CYAN}{_parser.ip}{Fore.RESET}' -> {Fore.LIGHTBLUE_EX}{domain}{Fore.RESET};\n"
        )

        if _parser.all:
            websites = _lookup._return(
                _parser.ip
            )

            if websites:
                print(
                    f'\n{Fore.MAGENTA}Other Websites hosted on the Server:{Fore.RESET}'
                )

                for website in websites:
                    print(
                        f"    > [ {Fore.GREEN}{website['last_resolved']}{Fore.RESET} ] : -> `{Fore.CYAN}{website['name']}{Fore.RESET}`"
                    )

                print('')

            else:
                print(
                    f"\n[ {Fore.RED}-{Fore.RESET }] : {Fore.LIGHTBLUE_EX}No Other Websites hosted on the Server{Fore.RESET}."
                )

    else:
        print(
            f"\n[ {Fore.RED}-{Fore.RESET} ] : {Fore.LIGHTRED_EX}No Domain Found for IP{Fore.RESET} : '{Fore.CYAN}{_parser.ip}{Fore.RESET}';\n"
        )


if __name__ == '__main__':
    main()
