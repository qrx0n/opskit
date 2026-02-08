from core.scanner import Scanner

from os import system
from colorama import Fore
from tabulate import tabulate
from sys import exit, platform
from socket import getservbyport



class Shell:
    def __init__(
        self, banner, slogan, 
        contacts):
        self.banner = banner
        self.slogan = slogan
        self.contacts = contacts

        self.usage = """Commands List:
=========== Basic Commands ===========
help - prints out this message (h, ?)
clear - cleans the terminal (;)
banner - prints out the banner
quit - close the tool (q, exit, close)

========== PunishNet Commands ==========
options - shows all available parameters
set - is used to set the parameter
run - executes the scanner"""


    def print_banner(
        self):
        print(Fore.RED + f"\n{self.banner}")
        print(Fore.YELLOW + self.slogan)


    def launch_shell(
        self):
        self.HOST = '127.0.0.1'
        self.PORTS = 65535

        while True:
            self.commandline = input(Fore.LIGHTMAGENTA_EX + f"💀punishnet >>> ")
            prompt = self.commandline.split()
            self.check_command(prompt)


    def check_command(
        self, command):

        if (len(command) == 0):
            pass

        else:
            if (command[0] == 'help'
                or command[0] == 'h'
                or command [0] == '?'):
                print(Fore.LIGHTCYAN_EX + f"\n{self.usage}\n")
            
            elif (command[0] == 'clear'
                or command[0] == ';'):
                if ('linux' in platform.lower()
                    or 'darwin' in platform.lower()):
                    system('clear')

                else:
                    system("cls")  

            elif (command[0] == 'banner'):
                self.print_banner()

            elif (command[0] == 'quit'
                or command[0] == 'close'
                or command[0] == 'exit'
                or command[0] == 'q'):
                exit(0)


            elif (command[0] == 'set'):
                if (command[1] == 'PORTS'):
                    if (self.PORTS > 0
                        and self.PORTS <= 65535):
                            self.PORTS = int(command[2])
                            print(Fore.LIGHTCYAN_EX + f"[+] PORTS parameter amount set to: {self.PORTS}.")

                    else:
                        print(Fore.RED + "[!] PORTS number must be between 1 and 65535.")
                
                elif (command[1] == 'HOST'):
                    self.HOST = str(command[2])
                    print(Fore.LIGHTCYAN_EX + f"[+] HOST parameter set to: {self.HOST}.")

                else:
                    print(Fore.RED + f"[!] There is no parameter named {command[1]}.")

            elif (command[0] == 'options'):
                opt = [
                    [
                    "HOST",
                    f"{self.HOST}",
                    "yes",
                    "The host you want to scan.",
                    ],
                    [
                    "PORTS",
                    f"{self.PORTS}",
                    "yes",
                    "Amount of ports to scan.",
                    ],
                    ]
                
                headers = [
                    "Name",
                    "Current Setting",
                    "Required",
                    "Description",
                ]

                self.options = tabulate(
                    opt, headers=headers,
                    tablefmt="simple")
                
                print("")
                print(Fore.LIGHTCYAN_EX + f"{self.options}\n")

            elif (command[0] == 'run'):
                #try:
                tmp = Scanner(self.HOST, self.PORTS)
                open_ports = tmp.scan_ports(
                                        tmp.target)
                
                headers = [
                    "Port",
                    "Service",
                ]

                data = []

                for port in open_ports:
                    try:
                        proto = getservbyport(port)
                    except:
                        proto = "undefind"
                    
                    data.append([port, proto])

                self.open_ports = tabulate(
                    data, headers=headers,
                    tablefmt="simple")

                
                print("")
                print(Fore.LIGHTCYAN_EX + f"{self.open_ports}\n")

#                except:
#                    print(Fore.RED + "[!] Check the HOST parameter accuracy.\nThe host is unreachable or isn't up.\nCheck your Internet Connection!")

            else:
                print(Fore.LIGHTYELLOW_EX + "[-] What? Try 'help'.")
