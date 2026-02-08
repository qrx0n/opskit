from time import sleep

from shodan import APIError
from dorkieye.utils.request.page import process

from dorkieye.config.colors import COLORS


def request_page(query, page, api):
    while True:
        try: 
            instances = api.search(
                query, 
                page=page
            )

            return instances
        
        except APIError as _err:
            print(
                f"{COLORS['ERR']}[!] ERROR : {_err}"
            )
            
            sleep(5)


def shodan(query, api):
    req = request_page(
        query,
        1,
        api
    )
    
    print(
        f"{COLORS['QUERY']}[*] QUERY: First Page"
    )

    total = req['total']

    processed = len(
        req['matches']
    )

    result = process(
        req
    )
    
    page = 2

    while processed < total:
        break

        print(
            f"{COLORS['QUERY']}[*] QUERY: Page {page}"
        )

        page = request_page(
            query,
            api,
            page=page,
        )

        processed += len(
            page['matches']
        )

        result = process(
            page
        )

        page += 1

    return result
