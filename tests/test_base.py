import unittest
from UnsplashAPI.base import UnsplashBase
import os

LOAD_FROM_ENV = True

if LOAD_FROM_ENV:
    access_keys = [os.environ['ACCESSKEY'], os.environ['ACCESSKEY2'], os.environ['ACCESSKEY3']]
else:
    with open('./tests/keys.txt', 'r') as txt_file:
        access_keys = [key for key in txt_file]

class TestUnsplashBase(unittest.TestCase):

    def test_init(self):
        base = UnsplashBase(access_key=access_keys[0])
        self.assertIsInstance(base, UnsplashBase)

    def test_check_api_con(self):
        base = UnsplashBase(access_key=access_keys[0])
        api_status = base._check_status()
        self.assertEqual(200, api_status)