import unittest
from urllib import response
from xmlrpc.client import ResponseError
from UnsplashAPI.api import UnsplashAPI
import os

access_keys = [os.environ['ACCESSKEY'], os.environ['ACCESSKEY2'], os.environ['ACCESSKEY3']]

class TestAPICollections(unittest.TestCase):
    """
    This class implements test for collection endpoint.
    This class only tests responses from endpoints with read access.
    """
    # Key
    access_key_idx = 0

    # Params
    page_limit = 2
    items_per_page = 5
    # Dict keys to check
    check_keys = ['id', 'title', 'description', 'published_at']
    # Check collection IDS
    collection_id = 2001768
    collection_title = 'Life in the Deep'

    # Init API
    api = UnsplashAPI(access_key=access_keys[access_key_idx])

    # General Test
    def test_init(self):
        self.assertIsInstance(self.api, UnsplashAPI)

    # Collections
    def test_collections_list_collections_paginate(self):
        response = self.api.list_collections_paginate(page_limit=self.page_limit, 
                                                        items_per_page=self.items_per_page)            
        try:
            results = []
            for element in response:
                results.append(element)
        except Exception:
            self.access_key_idx += 1
            print('Changed Key ID')
            if self.access_key_idx == len(access_keys):
                self.access_key_idx = 0
            self.api.access_key = access_keys[self.access_key_idx]
            results = []
            for element in response:
                results.append(element)

        self.assertEqual(self.page_limit, len(results))
        self.assertEqual(self.items_per_page, len(element))

    def test_collections_list_collection(self):
        try:    
            response = self.api.list_collection(page=1, items_per_page=self.items_per_page)
        except Exception:
            self.access_key_idx += 1
            print('Changed Key ID')
            if self.access_key_idx == len(access_keys):
                self.access_key_idx = 0
            self.api.access_key = access_keys[self.access_key_idx]
            response = self.api.list_collection(page=1, items_per_page=self.items_per_page)

        self.assertEqual(self.items_per_page, len(response))
        element = response[0]
        self.assertIsInstance(element, dict)
        for ckey in self.check_keys:
            self.assertIn(ckey, element.keys())
    
    def test_collections_get_collection_by_id(self):
        try:
            response = self.api.get_collection_by_id(collection_id=self.collection_id)
        except Exception:
            self.access_key_idx += 1
            print('Changed Key ID')
            if self.access_key_idx == len(access_keys):
                self.access_key_idx = 0
            self.api.access_key = access_keys[self.access_key_idx]
            response = self.api.get_collection_by_id(collection_id=self.collection_id)

        self.assertIsInstance(response, dict)
        self.assertEqual(response['id'], str(self.collection_id))
        self.assertEqual(response['title'], self.collection_title)
    
    def test_collection_get_collection_photos(self):
        response = self.api.get_collection_photos(collection_id=self.collection_id,
                                                    page_limit=self.page_limit, 
                                                    per_page=self.items_per_page)

        
        try:
            elements = []
            for element in response:
                elements.append(element)
        except Exception:
            self.access_key_idx += 1
            print('Changed Key ID')
            if self.access_key_idx == len(access_keys):
                self.access_key_idx = 0
            self.api.access_key = access_keys[self.access_key_idx]
            elements = []
            for element in response:
                elements.append(element)

        self.assertEqual(self.page_limit, len(elements))
        self.assertEqual(self.items_per_page, len(element))
        self.assertIsInstance(element[0], dict)
    
    def test_collections_get_related_collections(self):
        try:
            response = self.api.get_related_collections(collections_id=self.collection_id)
        except Exception:
            self.access_key_idx += 1
            print('Changed Key ID')
            if self.access_key_idx == len(access_keys):
                self.access_key_idx = 0
            self.api.access_key = access_keys[self.access_key_idx]
            response = self.api.get_related_collections(collections_id=self.collection_id)

        self.assertIsInstance(response, list)

        # Check keys in one response
        element = response[0]
        for ckey in self.check_keys:
            self.assertIn(ckey, element.keys())

    



        
        
