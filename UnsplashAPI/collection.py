import requests
from base import UnsplashBase


class UnsplashCollections(UnsplashBase):
    """
    This class implements API functionalities for the subcategory
    Collections.
    API-Doc: https://unsplash.com/documentation#list-collections
    """

    def __init__(self, access_key: str):
        """


        Args:
            access_key (str):       Access Key of the API
        """ 
        super().__init__(access_key=access_key)
        self.access_key = access_key


    def list_collections_paginate(self, page_limit: int = 10, items_per_page: int = 10):
        """
        Get a mulitple pages from collections.
        see here: https://unsplash.com/documentation#list-collections

        Parameters
        ----------
        page_limit:             Defines Iteration Limit, when iterating over multiple pages.
        items_per_page:         Defines how many items per page if multiple pages should be extracted

        Returns
        -------
        Iterator
        """
        endpoint = self.base_url + '/collections'
        for i in range(page_limit):
            response = self.session.get(endpoint,
                                        params=dict(client_id=self.access_key,
                                                    page=i,
                                                    per_page=items_per_page))
            if not response.status_code == 200:
                raise Exception(f'Not able to extract content. Code - {response.status_code}')

            yield response.json()

    def list_collection(self, page: int = 1, items_per_page: int = 10):
        """
        Get a single page from the Editorial feed.
        see here: https://unsplash.com/documentation#list-collections

        Parameters
        ----------
        page:                Page to extract data from 
        items_per_page:      Defines how many items per page should be extracted

        Returns
        -------
        Dictionary of Items
        """
        endpoint = self.base_url + '/collections'
        response = self.session.get(endpoint,
                                    params=dict(client_id=self.access_key,
                                                page=page,
                                                per_page=items_per_page))
        if not response.status_code == 200:
            raise Exception(f'Not able to extract content. Code - {response.status_code}')

        return response.json()

    def get_collection_by_id(self, collection_id):
        """
        Retrieve a collection by its ID.
        see here: https://unsplash.com/documentation#get-a-collection

        Parameters
        ----------
        collection_id:   ID of the photo

        Returns
        -------
        Dictionary of Items
        """
        endpoint = self.base_url + f'/collections/{collection_id}'
        response = self.session.get(endpoint,
                                    params=dict(client_id=self.access_key))
        if not response.status_code == 200:
            raise Exception(f'Not able to extract content. Code - {response.status_code}')

        return response.json()

    def get_collection_photos(self, collection_id, page_limit: int = 10, per_page: int = 10,
                               **kwargs):
        """
        Returns pageable object. More infos: https://unsplash.com/documentation#get-a-collections-photos

        Args:
            collection_id (_type_):             ID of the collection
            page_limit (int, optional):         Paginating Limit 
                                                Defaults to 10.
            per_page (int, optional):           Number of Elements per page
                                                Defaults to 10.
            **kwargs:                           see here https://unsplash.com/documentation#get-a-collections-photos

        Raises:
            Exception: Response Status

        Yields:
            Dictionary with Elements
        """
        endpoint = self.base_url + f'/collections/{collection_id}/photos'

        for i in range(page_limit):
            response = self.session.get(endpoint,
                                        params=dict(client_id=self.access_key,
                                                    page=i,
                                                    per_page=per_page, 
                                                    **kwargs))
            if not response.status_code == 200:
                raise Exception(f'Not able to extract content. Code - {response.status_code}')

            yield response.json()

    def get_related_collections(self, collections_id):
        """
        Retrieve a list of collections related to this one.
        see here: https://unsplash.com/documentation#list-a-collections-related-collections


        Args:
            collections_id (_type_):       ID of the collection

        Raises:
            Exception: Exception

        Returns:
            _type_: _description_
        """
        endpoint = self.base_url + f'/collections/{collections_id}/related'

        response = self.session.get(endpoint,
                                    params=dict(client_id=self.access_key))

        if not response.status_code == 200:
            raise Exception(f'Not able to extract content. Code - {response.status_code}')

        return response.json()

    def create_new_collection(self, title: str, **kwargs):
        """
        Create a new collection. This requires the write_collections scope.
        see here: https://unsplash.com/documentation#create-a-new-collection

        Args:
            title (str):        Title of the collection 
            kwargs;             see here: https://unsplash.com/documentation#create-a-new-collection

        Raises:
            Exception: Exception

        Returns:
            response: Responds with the new collection:
        """

        endpoint = self.base_url + f'/collections'
        response = self.session.post(endpoint,
                                     params=dict(client_id=self.access_key, 
                                                 title=title, **kwargs))
        if not response.status_code == 200:
            raise Exception(f'Not able to extract content. Code - {response.status_code}')

        return response.json()

    def update_photo(self, photo_id, **kwargs):
        endpoint = self.base_url + f'/photos/{photo_id}'
        response = self.session.put(endpoint,
                                    params=dict(client_id=self.access_key,
                                                **kwargs))

        return response.json()

    def update_collection(self, collections_id, **kwargs):
        """
        Update an existing collection belonging to the logged-in user. This requires the write_collections scope.
        see here: https://unsplash.com/documentation#update-an-existing-collection

        Args:
            collections_id:         Collection ID
            **kwargs                https://unsplash.com/documentation#update-an-existing-collection

        Returns:
            response: Responds with the new collection:
        """

        endpoint = self.base_url + f'/collections/{collections_id}'
        response = self.session.put(endpoint,
                                     params=dict(client_id=self.access_key, 
                                                **kwargs))

        return response.json()

    def delete_collection(self, collections_id):
        """
        Delete a collection belonging to the logged-in user. This requires the write_collections scope.
        see here: https://unsplash.com/documentation#delete-a-collection

        Args:
            collections_id (_type_): _description_

        Returns:
            response: Responds with a 204 status and an empty body.
        """
        endpoint = self.base_url + f'/collections/{collections_id}'
        response = self.session.delete(endpoint,
                                       params=dict(client_id=self.access_key))

        return response.json()

    def add_photo_to_collection(self, collections_id, photo_id):
        """
        Add a photo to one of the logged-in user’s collections. Requires the write_collections scope.

        see here; https://unsplash.com/documentation#add-a-photo-to-a-collection

        Note: If the photo is already in the collection, this acion has no effect.

        Args:
            collections_id (_type_):        ID of the collection
            photo_id (_type_):              Id of the image to add to the collection
        """
        endpoint = self.base_url + f'/collections/{collections_id}/add'
        response = self.session.post(endpoint,
                                       params=dict(client_id=self.access_key, 
                                                   photo_id=photo_id))

        return response.json()

    def remove_photo_from_collection(self, collections_id, photo_id):
        """
        Remove a photo from one of the logged-in user’s collections. Requires the write_collections scope.
        
        see here: https://unsplash.com/documentation#remove-a-photo-from-a-collection

        Args:
            collections_id (_type_):        ID of the collection
            photo_id (_type_):              ID of the photo to remove from collection.
        """
        endpoint = self.base_url + f'/collections/{collections_id}/remove'
        response = self.session.delete(endpoint,
                                       params=dict(client_id=self.access_key, 
                                                   photo_id=photo_id))

        return response.json()

    





