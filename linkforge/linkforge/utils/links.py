from requests import get
from bs4 import BeautifulSoup

from linkforge.utils.valid import valid

from urllib.parse import urlparse, urljoin

from linkforge.config.colors import COLORS


URLS = set(

)

INTERNAL_URLS = set(

)
    
EXTERNAL_URLS = set(

)


def links(url):
    soup = BeautifulSoup(
        get(
        url
        ).content,
        'html.parser'
    )

    domain_name = urlparse(
        url
    ).netloc

    for tag in soup.find_all('a'):
        href = tag.attrs.get(
            'href'
        )

        if href == '' or href is None:
            continue

        href = urljoin(url, href)
        parsed_href = urlparse(href)

        href = parsed_href.scheme + '://' + parsed_href.netloc + parsed_href.path

        if not valid(href):
            continue

        if href in INTERNAL_URLS:
            continue

        if domain_name not in href:
            if href not in EXTERNAL_URLS:
                EXTERNAL_URLS.add(
                    href
                )
                print(f'{COLORS["EXTERNAL"]}[-] External link: {href}{COLORS["RESET"]}')
            continue

        URLS.add(
            href
        )
        INTERNAL_URLS.add(
            href
        )

        print(f'{COLORS["INTERNAL"]}[+] Internal link: {href}{COLORS["RESET"]}')

    return URLS, [len(INTERNAL_URLS), len(EXTERNAL_URLS)]
