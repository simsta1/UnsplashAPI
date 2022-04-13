import unittest
from UnsplashAPI.collection import UnsplashCollections
from UnsplashAPI.photos import UnsplashPhotos, UnsplashSearch
from UnsplashAPI.topics_stats import UnsplashStats, UnsplashTopics
from UnsplashAPI.user import UnsplashUsers
import os

# Get Credentials for API
LOAD_FROM_ENV = True

if LOAD_FROM_ENV:
    access_keys = [os.environ['ACCESSKEY'], os.environ['ACCESSKEY2'], os.environ['ACCESSKEY3']]
else:
    with open('./tests/keys.txt', 'r') as txt_file:
        access_keys = [key for key in txt_file]

class TestUnsplashCollections(unittest.TestCase):
    
    def test_init(self):
        self.api = UnsplashCollections(access_key=access_keys[0])
        self.assertIsInstance(self.api, UnsplashCollections)

class TestUnsplashPhotos(unittest.TestCase):
    
    def test_init(self):
        self.api = UnsplashPhotos(access_key=access_keys[0])
        self.assertIsInstance(self.api, UnsplashPhotos)

class TestUnsplashSearch(unittest.TestCase):
    
    def test_init(self):
        self.api = UnsplashSearch(access_key=access_keys[0])
        self.assertIsInstance(self.api, UnsplashSearch)

class TestUnsplashStats(unittest.TestCase):

    def test_init(self):
        self.api = UnsplashStats(access_key=access_keys[0])
        self.assertIsInstance(self.api, UnsplashStats)

class TestUnsplashTopics(unittest.TestCase):
    
    def test_init(self):
        self.api = UnsplashTopics(access_key=access_keys[0])
        self.assertIsInstance(self.api, UnsplashTopics)

class TestUnplashUsers(unittest.TestCase):
    
    def test_init(self):
        self.api = UnsplashUsers(access_key=access_keys[0])
        self.assertIsInstance(self.api, UnsplashUsers)

