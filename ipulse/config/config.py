from json import loads


def read_config(file_path: str):
    with open(
        file=file_path,
        mode='r'
    ) as config:
        data = loads(
            config.read()
        )

        config.close()

    return data['token']
