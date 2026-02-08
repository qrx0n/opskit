CONFIG = {
    'interface': None,
    'mac_addr': None,
    'timeout': None,
    'random': None,
}


def check_args(args):
    CONFIG['interface'] = args.interface

    if args.random:
        CONFIG['random'] = args.random
        CONFIG['timeout'] = int(args.timeout)

    elif args.mac_addr:
        CONFIG['mac_addr'] = args.mac_addr

    return CONFIG
