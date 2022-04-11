import requests
from .base import UnsplashBase


class UnsplashPhotos(UnsplashBase):
    """
    This class implements API functionalities for the subcategory
    Photos.
    API-Doc: https://unsplash.com/documentation#list-photos
    """

    def __init__(self, access_key: str):
        """


        Args:
            access_key (str):           Access Key given from the API
        """
        super().__init__(access_key=access_key)
        self.access_key = access_key

    def list_photos_paginate(self, page_limit: int = 10, items_per_page: int = 10, **kwargs):
        """
        Get a mulitple pages from the Editorial feed.
        see here: https://unsplash.com/documentation#list-photos

        Args:
            page_limit (int, optional):     Defines Iteration Limit, when iterating over multiple pages. 
                                            Defaults to 10.
            items_per_page (int, optional): Defines how many items per page if multiple pages should be extracted
                                            Defaults to 10.
            **kwargs:
                    order_by: str = 'latest'

        Raises:
            Exception: Exception

        Yields:
            Dictionary with page contents: 
        """  
        endpoint = self.base_url + '/photos'
        for i in range(page_limit):
            response = self.session.get(endpoint,
                                        params=dict(client_id=self.access_key,
                                                    page=i,
                                                    per_page=items_per_page))
            if not response.status_code == 200:
                raise Exception(f'Not able to extract content. Code - {response.status_code}')

            yield response.json()

    def list_photos(self, items_per_page: int = 10, **kwargs):
        """
        Get a single page from the Editorial feed.
        see here: https://unsplash.com/documentation#list-photos

        Parameters
        ----------
        items_per_page:      Defines how many items per page if multiple pages should be extracted
        **kwargs:
                order_by: str = 'latest'

        Returns
        -------
        Dictionary of Items
        """
        endpoint = self.base_url + '/photos'
        response = self.session.get(endpoint,
                                    params=dict(client_id=self.access_key,
                                                page=1,
                                                per_page=items_per_page, **kwargs))
        if not response.status_code == 200:
            raise Exception(f'Not able to extract content. Code - {response.status_code}')

        return response.json()

    def get_photo_by_id(self, photo_id):
        """
        Retrieve a single photo.
        see here: https://unsplash.com/documentation#get-a-photo

        Parameters
        ----------
        photo_id:       ID of the photo
                        (see @ end of url if photo openend in browser)

        Returns
        -------
        Dictionary of Items
        """
        endpoint = self.base_url + f'/photos/{photo_id}'
        response = self.session.get(endpoint,
                                    params=dict(client_id=self.access_key))
        if not response.status_code == 200:
            raise Exception(f'Not able to extract content. Code - {response.status_code}')

        return response.json()

    def get_random_photo(self, **kwargs):
        """
        Returns a random photo.
        see here: https://unsplash.com/documentation#get-a-random-photo


        Parameters
        ----------
        kwargs:
            collections:	Public collection ID(‘s) to filter selection. If multiple, comma-separated
            topics:	        Public topic ID(‘s) to filter selection. If multiple, comma-separated
            username:	    Limit selection to a single user.
            query:	        Limit selection to photos matching a search term.
            orientation:	Filter by photo orientation. (Valid values: landscape, portrait, squarish)
            content_filter:	Limit results by content safety. Default: low. Valid values are low and high.
            count:	        The number of photos to return. (Default: 1; max: 30)

        Returns
        -------
        Dictionary of Items
        """
        endpoint = self.base_url + '/photos/random'
        response = self.session.get(endpoint,
                                    params=dict(client_id=self.access_key, **kwargs))
        if not response.status_code == 200:
            raise Exception(f'Not able to extract content. Code - {response.status_code}')

        return response.json()

    def get_photo_statistics(self, photo_id):
        """
        Retrieves statistics of a single photo.
        see here: https://unsplash.com/documentation#get-a-photos-statistics

        Parameters
        ----------
        photo_id:       ID of the photo
                        (see @ end of url if photo openend in browser)

        Returns
        -------
        Dictionary of Items
        """
        endpoint = self.base_url + f'/photos/{photo_id}/statistics'
        response = self.session.get(endpoint,
                                    params=dict(client_id=self.access_key))
        if not response.status_code == 200:
            raise Exception(f'Not able to extract content. Code - {response.status_code}')

        return response.json()

    def track_photo_download(self, photo_id):
        """
        Tracks donwload of a photo.

        see here: https://unsplash.com/documentation#track-a-photo-download

        Parameters
        ----------
        photo_id:       ID of the photo
                        (see @ end of url if photo openend in browser)

        Returns
        -------
        Dictionary of Items
        """
        endpoint = self.base_url + f'/photos/{photo_id}/download'
        response = self.session.get(endpoint,
                                    params=dict(client_id=self.access_key))
        if not response.status_code == 200:
            raise Exception(f'Not able to extract content. Code - {response.status_code}')

        return response.json()

    def update_photo(self, photo_id, **kwargs):
        """
        Updating a user photo. Requires Write Access for user profile (API-Settings)
        see here: https://unsplash.com/documentation#update-a-photo

        Parameters
        ----------
        photo_id:       ID of the photo
                        (see @ end of url if photo openend in browser)
        kwargs:
                id	                    The photo’s ID. Required.
                description	            The photo’s description (Optional).
                show_on_profile	        The photo’s visibility (Optional).
                tags	                The photo’s tags (Optional).
                location[latitude]	    The photo location’s latitude rounded to 6 decimals. (Optional)
                location[longitude]	    The photo location’s longitude rounded to 6 decimals. (Optional)
                location[name]	        The photo’s full location string (including city and country) (Optional)
                location[city]	        The photo location’s city (Optional)
                location[country]	    The photo location’s country (Optional)
                exif[make]	            Camera’s brand (Optional)
                exif[model]	            Camera’s model (Optional)
                exif[exposure_time]	    Camera’s exposure time (Optional)
                exif[aperture_value]	Camera’s aperture value (Optional)
                exif[focal_length]	    Camera’s focal length (Optional)
                exif[iso_speed_ratings]	Camera’s iso (Optional)

        Returns
        -------
        Dictionary of Items
        """
        endpoint = self.base_url + f'/photos/{photo_id}'
        response = self.session.put(endpoint,
                                    params=dict(client_id=self.access_key,
                                                **kwargs))

        return response.json()

    def like_photo(self, photo_id):
        """
        Likes a photo. Needs write access within API-settings.
        see here: https://unsplash.com/documentation#like-a-photo

        Parameters
        ----------
        photo_id:       ID of the photo
                        (see @ end of url if photo openend in browser)

        Returns
        -------
        Dictionary of Items
        """
        endpoint = self.base_url + f'/photos/{photo_id}/like'
        response = self.session.post(endpoint,
                                     params=dict(client_id=self.access_key))

        return response.json()

    def unlike_photo(self, photo_id):
        """
        Unlikes a photo. Needs write access in API settings.
        see here: https://unsplash.com/documentation#unlike-a-photo

        Parameters
        ----------
        photo_id:       ID of the photo
                        (see @ end of url if photo openend in browser)

        Returns
        -------
        Dictionary of Items
        """
        endpoint = self.base_url + f'/photos/{photo_id}/like'
        response = self.session.delete(endpoint,
                                       params=dict(client_id=self.access_key))

        return response.json()


class UnsplashSearch(UnsplashBase):
    """
    This class wraps the Search endpoint of the API.
    Docs: https://unsplash.com/documentation#search
    """

    def __init__(self, access_key: str) -> None:
        super().__init__(access_key=access_key)

    def search_photos(self, query: str, number_of_pages: int = 1, items_per_page: int = 10, **kwargs) -> iter:
        """
        Get a single page of photo results for a query.
        see here: https://unsplash.com/documentation#search

        Args:
            query (str):               Search Query
            number_of_pages (int):     Number of pages to retrieve.
                                       Default 1
            items_per_page (int):      Number of items per page
                                       Default: 10
            **kwargs:
                    per_page: Number of items per page. (Optional; default: 10)
                    order_by: How to sort the photos. (Optional; default: relevant). Valid values are latest and relevant.
                    collections	Collection ID(‘s) to narrow search. Optional. If multiple, comma-separated.
                    content_filter	Limit results by content safety. (Optional; default: low). Valid values are low and high.
                    color	Filter results by color. Optional. Valid values are: black_and_white, black, white, yellow, orange, red, purple, magenta, green, teal, and blue.
                    orientation	Filter by photo orientation. Optional. (Valid values: landscape, portrait, squarish)

        Returns:
            iter:                      Generator containing all elements.
        """
        endpoint = self.base_url + '/search/photos'
        for i in range(number_of_pages):
            response = self.session.get(endpoint,
                                        params=dict(client_id=self.access_key,
                                                    query=query,
                                                    page=i, 
                                                    per_page=items_per_page, 
                                                    **kwargs))
            if not response.status_code == 200:
                raise Exception(f'Not able to extract content. Code - {response.status_code}')

            yield response.json()

    def search_collections(self, query: str, number_of_pages: int = 1, items_per_page: int = 10) -> iter:
        """
        Get a single page of collection results for a query.
        see here:  https://unsplash.com/documentation#search-collections


        Args:
            query (str):                        Search query
            number_of_pages (int, optional):    Number of pages to retrieve.
                                                Defaults to 1.
            items_per_page (int, optional):     Number of items per page
                                                Defaults to 10.                        

        Returns:
            iter:               Generator containing all elements
        """
        endpoint = self.base_url + '/search/collections'
        for i in range(number_of_pages):
            response = self.session.get(endpoint,
                                        params=dict(client_id=self.access_key,
                                                    query=query,
                                                    page=i, 
                                                    per_page=items_per_page))
            if not response.status_code == 200:
                raise Exception(f'Not able to extract content. Code - {response.status_code}')

            yield response.json()


    def search_users(self, query: str, number_of_pages: int = 1, items_per_page: int = 10) -> iter:
        """
        Get a single page of user results for a query.
        see here:  https://unsplash.com/documentation#search-users


        Args:
            query (str):                        Search query
            number_of_pages (int, optional):    Number of pages to retrieve.
                                                Defaults to 1.
            items_per_page (int, optional):     Number of items per page
                                                Defaults to 10.                        

        Returns:
            iter:               Generator containing all elements
        """
        endpoint = self.base_url + '/search/users'
        for i in range(number_of_pages):
            response = self.session.get(endpoint,
                                        params=dict(client_id=self.access_key,
                                                    query=query,
                                                    page=i, 
                                                    per_page=items_per_page))
            if not response.status_code == 200:
                raise Exception(f'Not able to extract content. Code - {response.status_code}')

            yield response.json()
    










