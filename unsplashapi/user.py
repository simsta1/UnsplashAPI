import requests
from .base import UnsplashBase


class UnsplashUsers(UnsplashBase):
    """
    Wraps the API methods of Users
    see here: https://unsplash.com/documentation#users
    """
    def __init__(self, access_key: str):
        """
        Args:
            access_key (str):        Access key of the API.
        """
        super().__init__(access_key=access_key)
        self.access_key = access_key

    def get_current_user(self) -> dict:
        """
        Retrieve public details on a given user.

        Raises:
            Exception: Excepion

        Returns:
            Dictionary:     Dict with profile contents.
        """
        endpoint = self.base_url + '/me'
        response = self.session.get(endpoint,
                                    params=dict(client_id=self.access_key))
        if not response.status_code == 200:
            raise Exception(f'Not able to extract content. Code - {response.status_code}')

        return response.json()

    def get_user_profile(self, username: str) -> dict:
        """
        Retrieve public details on a given user.

        Args:
            username (str):   Username 

        Raises:
            Exception: Exception

        Returns:
            Dict:  Dict containing profile elements
        """
        endpoint = self.base_url + f'/users/{username}'
        response = self.session.get(endpoint,
                                    params=dict(client_id=self.access_key))
        if not response.status_code == 200:
            raise Exception(f'Not able to extract content. Code - {response.status_code}')

        return response.json()

    def get_user_portfolio_link(self, username: str) -> dict:
        """
        Retrieve a single user’s portfolio link.
        see here: https://unsplash.com/documentation#get-a-users-portfolio-link

        Args:
            username (str):  Name of the user

        Raises:
            Exception: Exception

        Returns:
            dict:               dict containing portfolio link.
        """
        endpoint = self.base_url + f'/users/{username}/portfolio'
        response = self.session.get(endpoint,
                                    params=dict(client_id=self.access_key))
        if not response.status_code == 200:
            raise Exception(f'Not able to extract content. Code - {response.status_code}')

        return response.json()

    def list_user_photos(self, username: str) -> dict:
        """
        Get a list of photos uploaded by a user.
        see here: https://unsplash.com/documentation#list-a-users-photos

        Args:
            username (str):     Name of the user

        Raises:
            Exception: Exception

        Returns:
            dict:               dict containing all photos of a user.
        """
        endpoint = self.base_url + f'/users/{username}/photos'
        response = self.session.get(endpoint,
                                    params=dict(client_id=self.access_key))
        if not response.status_code == 200:
            raise Exception(f'Not able to extract content. Code - {response.status_code}')

        return response.json()

    def list_user_liked_photos(self, username: str) -> dict:
        """
        Get a list of photos liked by a user.
        see here: https://unsplash.com/documentation#list-a-users-liked-photos

        Args:
            username (str):     Name of the user

        Raises:
            Exception: Exception

        Returns:
            dict:               Liked photos of the user.
        """
        endpoint = self.base_url + f'/users/{username}/likes'
        response = self.session.get(endpoint,
                                    params=dict(client_id=self.access_key))
        if not response.status_code == 200:
            raise Exception(f'Not able to extract content. Code - {response.status_code}')

        return response.json()

    def list_user_liked_collections(self, username: str) -> dict:
        """
        Get a list of collections created by the user.
        see here; https://unsplash.com/documentation#list-a-users-collections

        Args:
            username (str):     Name of the user

        Raises:
            Exception: Exceptino

        Returns:
            dict:               Liked collections
        """

        endpoint = self.base_url + f'/users/{username}/collections'
        response = self.session.get(endpoint,
                                    params=dict(client_id=self.access_key))
        if not response.status_code == 200:
            raise Exception(f'Not able to extract content. Code - {response.status_code}')

        return response.json()

    def get_user_statistics(self, username: str) -> dict:
        """
        Retrieve the consolidated number of downloads, views and likes of all user’s photos, 
        as well as the historical breakdown and average of these stats in a specific timeframe (default is 30 days).
        see here: https://unsplash.com/documentation#get-a-users-statistics

        Args:
            username (str):         Name of user

        Raises:
            Exception: Exception

        Returns:
            dict:                   User stats
        """
        endpoint = self.base_url + f'/users/{username}/statistics'
        response = self.session.get(endpoint,
                                    params=dict(client_id=self.access_key))
        if not response.status_code == 200:
            raise Exception(f'Not able to extract content. Code - {response.status_code}')

        return response.json()





