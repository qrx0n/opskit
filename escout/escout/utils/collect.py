from re import finditer

from escout.config.config import CONFIG
from escout.utils.response import response


def collect(response):
    data = [

    ]


    for re_match in finditer(
        CONFIG['email_regex'], 
        response.html.raw_html.decode()
    ):
        data.append(
            re_match.group()
        )

    return data
