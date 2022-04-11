import requests


class UnsplashBase:

    base_url = 'https://api.unsplash.com/'

    def __init__(self, access_key: str) -> None:
        super().__init__()
        self.access_key = access_key
        self.session = requests.Session()
        self.check_status()

    def check_status(self):
        response = self.session.get(self.base_url)
        assert response.status_code == 200, f'API not reachable Code: {response.status_code}'