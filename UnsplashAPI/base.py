import requests


class UnsplashBase:

    base_url = 'https://api.unsplash.com/'
    fixed_profile = 'simonstaehli'

    def __init__(self, access_key: str) -> None:
        super().__init__()
        self.access_key = access_key
        self.session = requests.Session()
        self._check_status()
        

    def _check_status(self):
        """
        Checks if the API is reachable.

        Returns:
            API Status Code:    200 if everything is OK. 
        """
        response = self.session.get(self.base_url)
        assert response.status_code == 200, f'API not reachable Code: {response.status_code}'

        return response.status_code

    def get_current_rate_limit(self):
        """
        Returns the current rate Limit

        Returns:
            Remaining Requests.
        """
        response = requests.get(f'https://api.unsplash.com/users/{self.fixed_profile}', 
                                params=dict(client_id=self.access_key))
        response_headers = dict(response.headers)

        return response_headers.get('X-Ratelimit-Remaining')