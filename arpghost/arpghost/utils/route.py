from arpghost.config.colors import COLORS


def enable():
    with open('/proc/sys/net/ipv4/ip_forward') as file:
        if file.read() == 1:
            return
        
    
    with open('/proc/sys/net/ipv4/ip_forward', 'w') as file:
        print(
            1,
            file=file
        )



def route(verbose=True):
    if verbose:
        print(
            f"{COLORS['RESET']}[!] {COLORS['ROUTE']}Enabling IP Routing..."
        )

    enable()

    if verbose:
        print(
            f"{COLORS['RESET']}[!] {COLORS['ROUTE']}IP Routing enabled."
        )
