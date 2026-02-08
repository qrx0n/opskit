from configparser import ConfigParser


class Config:
    def __init__(self, _file) -> None:
        self.config = ConfigParser()
        self.config.read(_file)


    def _return(self, section, element):
        return self.config.get(
            section=section,
            option=element
        )
