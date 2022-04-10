import requests


class UnsplashBase(object):

    def __init__(self) -> None:
        self.session = requests.Session()