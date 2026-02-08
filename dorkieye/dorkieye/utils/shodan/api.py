from shodan import Shodan


def api(key):
    return Shodan(
        key
    )
