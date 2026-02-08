from urllib.parse import urlparse


def valid(url: str):
    parse = urlparse(url)

    return bool(parse.netloc) and bool(parse.scheme)
