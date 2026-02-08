from subprocess import check_output

from macmorphy.config.commands import COMMANDS


def change(iface: str, mac: str):
    check_output(
        f'{COMMANDS["get_config"]} {iface} {COMMANDS["shutdown"]}',
        shell=True
    )

    check_output(
        f'{COMMANDS["get_config"]} {iface} {COMMANDS["change_mac"]} {mac}',
        shell=True
    )

    check_output(
        f'{COMMANDS["get_config"]} {iface} {COMMANDS["rise_up"]}',
        shell=True
    )
