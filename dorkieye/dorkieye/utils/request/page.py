from dorkieye.config.colors import COLORS

from dorkieye.utils.request.credentials import valid_credentials


def process(page):
    result = [

    ]

    for instance in page['matches']:
        if valid_credentials(instance):
            print(
                f"{COLORS['CREDENTIALS']}[+] VALID CREDENTIALS FOUND : {COLORS['RESET']}'{COLORS['QUERY']}{instance['ip_str']}{COLORS['RESET']}':'{COLORS['QUERY']}{instance['port']}{COLORS['RESET']}'"
            )

            result.append(
                instance
            )

    return result
