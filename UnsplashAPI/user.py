import requests
from base import UnsplashBase


class UnsplashUsers(UnsplashBase):

    def __init__(self, access_key):
        """"""
        super().__init__()
        self.access_key = access_key

    def get_current_user(self):
        endpoint = self.base_url + '/me'
        response = self.session.get(endpoint,
                                    params=dict(client_id=self.access_key))
        if not response.status_code == 200:
            raise Exception(f'Not able to extract content. Code - {response.status_code}')

        return response.json()

    def get_user_profile(self, username):
        endpoint = self.base_url + f'/users/{username}'
        response = self.session.get(endpoint,
                                    params=dict(client_id=self.access_key))
        if not response.status_code == 200:
            raise Exception(f'Not able to extract content. Code - {response.status_code}')

        return response.json()

    def get_user_portfolio_link(self, username):
        endpoint = self.base_url + f'/users/{username}/portfolio'
        response = self.session.get(endpoint,
                                    params=dict(client_id=self.access_key))
        if not response.status_code == 200:
            raise Exception(f'Not able to extract content. Code - {response.status_code}')

        return response.json()

    def list_user_photos(self, username):
        endpoint = self.base_url + f'/users/{username}/photos'
        response = self.session.get(endpoint,
                                    params=dict(client_id=self.access_key))
        if not response.status_code == 200:
            raise Exception(f'Not able to extract content. Code - {response.status_code}')

        return response.json()

    def list_user_liked_photos(self, username):
        endpoint = self.base_url + f'/users/{username}/likes'
        response = self.session.get(endpoint,
                                    params=dict(client_id=self.access_key))
        if not response.status_code == 200:
            raise Exception(f'Not able to extract content. Code - {response.status_code}')

        return response.json()

    def list_user_liked_collections(self, username):
        endpoint = self.base_url + f'/users/{username}/collections'
        response = self.session.get(endpoint,
                                    params=dict(client_id=self.access_key))
        if not response.status_code == 200:
            raise Exception(f'Not able to extract content. Code - {response.status_code}')

        return response.json()

    def get_user_statistics(self, username):
        endpoint = self.base_url + f'/users/{username}/statistics'
        response = self.session.get(endpoint,
                                    params=dict(client_id=self.access_key))
        if not response.status_code == 200:
            raise Exception(f'Not able to extract content. Code - {response.status_code}')

        return response.json()





