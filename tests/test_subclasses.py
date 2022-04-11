import unittest
#import sys
#sys.path.append('..')
from ..UnsplashAPI.collection import UnsplashCollections
from ..UnsplashAPI.photos import UnsplashPhotos, UnsplashSearch
from ..UnsplashAPI.topics_stats import UnsplashStats, UnsplashTopics
from ..UnsplashAPI.user import UnsplashUsers
import os

# Get Credentials for API
access_key = os.environ['ACCESSKEY']

class TestUnsplashCollections(unittest.TestCase):
    
    def test_init(self):
        self.api = UnsplashCollections(access_key=access_key)
        self.assertIsInstance(self.api, UnsplashCollections)

class TestUnsplashPhotos(unittest.TestCase):
    
    def test_init(self):
        self.api = UnsplashPhotos(access_key=access_key)
        self.assertIsInstance(self.api, UnsplashPhotos)

class TestUnsplashSearch(unittest.TestCase):
    
    def test_init(self):
        self.api = UnsplashSearch(access_key=access_key)
        self.assertIsInstance(self.api, UnsplashSearch)

class TestUnsplashStats(unittest.TestCase):

    def test_init(self):
        self.api = UnsplashStats(access_key=access_key)
        self.assertIsInstance(self.api, UnsplashStats)

class TestUnsplashTopics(unittest.TestCase):
    
    def test_init(self):
        self.api = UnsplashTopics(access_key=access_key)
        self.assertIsInstance(self.api, UnsplashTopics)

class TestUnplashUsers(unittest.TestCase):
    
    def test_init(self):
        self.api = UnsplashUsers(access_key=access_key)
        self.assertIsInstance(self.api, UnsplashUsers)

