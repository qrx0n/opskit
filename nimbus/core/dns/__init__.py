from requests import get # type: ignore

from ipaddress import ip_address
from socket import gethostbyaddr, herror


class Lookup:
    def __init__(self, api) -> None:
        self.api = api


    def valid(self, ip) -> bool:
        try:
            ip_address(
                ip
            )
            return True

        except ValueError:
            return False


    def lookup(self, ip) -> str:
        try:
            _ = gethostbyaddr(
                ip
            )[0]
            return _

        except herror:
            return None


    def _return(self, ip) -> list:
        uri = f"https://api.viewdns.info/reverseip/?host={ip}&apikey={self.api}&output=json"

        response = get(
            url=uri
        )

        if (response.status_code == 200):
            data = response.json()

            if ('response' in data
                and 'domains' in data['response']):
                return data['response']['domains']

        return []
