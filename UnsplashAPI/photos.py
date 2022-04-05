import requests


class UnsplashPhotos(object):
    """
    This class implements API functionalities for the subcategory
    Photos.
    API-Doc: https://unsplash.com/documentation#list-photos
    """

    base_url = 'https://api.unsplash.com/'

    def __init__(self, access_key: str, order_by: str = 'latest'):
        """

        Parameters
        ----------
        access_key:             Access Key given from the API
        order_by:               Defines the ordering of the images:
                                latest, oldest, popular; default: latest
        """
        self.access_key = access_key
        self.order_by = order_by
        self.session = requests.Session()

    def list_photos_paginate(self, page_limit: int = 10, items_per_page: int = 10):
        """
        Get a mulitple pages from the Editorial feed.
        see here: https://unsplash.com/documentation#list-photos

        Parameters
        ----------
        page_limit:             Defines Iteration Limit, when iterating over multiple pages.
        items_per_page:         Defines how many items per page if multiple pages should be extracted

        Returns
        -------
        Iterator
        """
        endpoint = self.base_url + '/photos'
        for i in range(page_limit):
            response = self.session.get(endpoint,
                                        params=dict(client_id=self.access_key,
                                                    page=i, order_by=self.order_by,
                                                    per_page=items_per_page))
            if not response.status_code == 200:
                raise Exception(f'Not able to extract content. Code - {response.status_code}')

            yield response.json()

    def list_photos(self, items_per_page: int = 10):
        """
        Get a single page from the Editorial feed.
        see here: https://unsplash.com/documentation#list-photos

        Parameters
        ----------
        items_per_page:      Defines how many items per page if multiple pages should be extracted

        Returns
        -------
        Dictionary of Items
        """
        endpoint = self.base_url + '/photos'
        response = self.session.get(endpoint,
                                    params=dict(client_id=self.access_key,
                                                page=1, order_by=self.order_by,
                                                per_page=items_per_page))
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





