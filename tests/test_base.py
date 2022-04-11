import unittest
import sys
sys.path.append('..')
from UnsplashAPI.base import UnsplashBase

class TestUnsplashBase(unittest.TestCase):
    # How to load access key
    access_key = ''

    def test_init(self):
        base = UnsplashBase(access_key=self.access_key)
        self.assertIsInstance(base, UnsplashBase)

    def test_check_api(self):
        base = UnsplashBase(access_key=self.access_key)
        base.check_status()