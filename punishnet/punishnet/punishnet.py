from os import system
from sys import platform
from colorama import Fore

from core.shell import Shell
from core.banner import BANNER, CONTACTS, SLOGAN

def banner():
    if ('linux' in platform.lower()
        or 'darwin' in platform.lower()):
        system('clear')

    else:
        system("cls")  
    
    print(Fore.LIGHTRED_EX + BANNER)
    print(Fore.YELLOW + SLOGAN)

def contacts():
    print(Fore.LIGHTGREEN_EX + CONTACTS)

def main():
    try:
        banner()
        contacts()

        # launch panishnet
        panisher = Shell(
                        BANNER, SLOGAN, CONTACTS)
        panisher.launch_shell()
    
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
