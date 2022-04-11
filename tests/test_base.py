import unittest
import sys
sys.path.append('..')
from UnsplashAPI.base import UnsplashBase
import os

access_key = os.environ['ACCESSKEY']

class TestUnsplashBase(unittest.TestCase):

    def test_init(self):
        base = UnsplashBase(access_key=access_key)
        self.assertIsInstance(base, UnsplashBase)

    def test_check_api_con(self):
        base = UnsplashBase(access_key=access_key)
        api_status = base.check_status()
        self.assertEqual(200, api_status)