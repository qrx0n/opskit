from re import search

from requests import Session
from requests.exceptions import ConnectionError

from dorkieye.config.colors import COLORS


def valid_credentials(instance):
    session = Session()

    proto = ('ssl' in instance) and 'https' or 'http'

    try:
        res = session.get(
            f"{proto}://{instance['ip_str']}:{instance['port']}/login.php",
            verify=False
        )

    except ConnectionError:
        return False
    

    if res.status_code != 200:
        print(
            f"{COLORS['ERR']}[!] ERROR : Got HTTP status code {res.status_code}, expected 200"
        )

        return False
    

    token = search(
        r"user_token' value='([0-9a-f]+)'",
        res.text
    ).group(
        1
    )

    res = session.post(
        f"{proto}://{instance['ip_str']}:{instance['port']}/login.php",
        f"username=admin&password=password&user_token={token}&Login=Login",
        allow_redirects=False,
        verify=False,
        headers={
            'Content-Type': 'application/x-www-form-urlencoded'
        }
    )

    if res.status_code == 302 and res.headers['Location'] == 'index.php':
        return True
    
    else:
        return False
