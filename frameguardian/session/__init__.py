from requests import get
from requests.exceptions import RequestException

from colorama import Fore

class Session:
    def __init__(self, uri) -> None:
        try:
            if (uri.startswith('http://')):
                self.uri = 'https://' + uri[len('http://'):]

            elif (uri.startswith('https://')):
                self.uri = uri

            else:
                self.uri = 'https://' + uri

        except RequestException as _rqex:
            print(
                f"\n[ {Fore.RED}*{Fore.RESET} ] An Error occurred, while checking '{Fore.CYAN}{uri}{Fore.RESET}' -> `{_rqex}`\n" # type: ignore
            )

            raise Exception(
                'Program terminated due to an error.'
            )

        self.response = get(
            self.uri
        )

        self.headers = self.response.headers


    def _xframe(self) -> bool:
        if ('X-Frame-Options' not in self.headers):
            return True

        frame = self.headers['X-Frame-Options'].lower()

        if (frame != 'deny'
            and frame != 'sameorigin'):
            return True

        return False


    def _headers(self) -> dict:
        return self.headers
