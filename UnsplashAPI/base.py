import requests


class UnsplashBase(object):

    base_url = 'https://api.unsplash.com/'

    def __init__(self) -> None:
        self.session = requests.Session()