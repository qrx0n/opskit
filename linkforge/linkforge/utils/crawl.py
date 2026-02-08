from linkforge.utils.links import links

from linkforge.config.colors import COLORS


def crawl(url):
    print(
        f'{COLORS["CRAWL"]}[*] Crawling: {url}{COLORS["RESET"]}'
    )

    links_ = links(
        url
    )

    return links_[1][0], links_[1][1]
