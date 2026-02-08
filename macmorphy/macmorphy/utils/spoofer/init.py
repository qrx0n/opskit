from random import choice
from string import hexdigits

from re import search
from subprocess import check_output

from macmorphy.config.hex import DIGITS
from macmorphy.config.commands import COMMANDS


def random():
    upper_hexdigits = ''.join(
        set(hexdigits.upper())
    )

    addr = ''

    for mac in range(6):
        for hex in range(2):
            if mac == 0:
                addr += choice(
                    DIGITS
                )

            else:
                addr += choice(
                    upper_hexdigits
                )

        addr += ':'

    return addr.strip(
        ':'
    )


def current(iface: str):
    output = check_output(
        f'{COMMANDS["get_config"]} {iface}',
        shell=True
    ).decode()

    return search(
        f'{COMMANDS["find_mac"]}',
        output
    ).group().split()[1].strip()
