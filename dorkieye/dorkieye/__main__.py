from config.config import read_config

from dorkieye.utils.banner.banner import init

from dorkieye.utils.argparser.parser import parser

from dorkieye.utils.shodan.api import api
from dorkieye.utils.shodan.queries import shodan


def main():
    args = parser(

    )

    init()

    token = read_config(
        args.config
    )

    api_ = api(
        token
    )

    result = shodan(
        query='title:dvwa',
        api=api_
    )

    print(
        result
    )


if __name__ == '__main__':
    main()
