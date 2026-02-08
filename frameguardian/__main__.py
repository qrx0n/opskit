from colorama import Fore

from frameguardian.session import Session
from frameguardian.arguments import parser


def main():
    _parser = parser()

    _uri = _parser.uri

    _session = Session(
        uri=_uri
    )

    _vulnv = _session._xframe()

    if (_vulnv):
        print(
            f"\n[ {Fore.GREEN}+{Fore.RESET} ]: {Fore.LIGHTGREEN_EX}URI{Fore.RESET} : '{Fore.CYAN}{_uri}{Fore.RESET}' -> {Fore.LIGHTBLUE_EX}might be vulnerable{Fore.RESET};"
        )

    else:
        print(
            f"\n[ {Fore.RED}-{Fore.RESET} ]: {Fore.LIGHTRED_EX}URI{Fore.RESET} : '{Fore.CYAN}{_uri}{Fore.RESET}' -> {Fore.LIGHTBLUE_EX}seems to be clear{Fore.RESET};"
        )

    if _parser.log:
        _headers = _session._headers()

        print(f'\n{Fore.MAGENTA}Response Headers:{Fore.RESET}')

        for header, value in _headers.items():
            print(f'    > {Fore.GREEN}{header}{Fore.RESET} : -> `{Fore.CYAN}{value}`{Fore.RESET}')

        print('')

if __name__ == '__main__':
    main()
