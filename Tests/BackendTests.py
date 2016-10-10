import unittest
from unittest.mock import MagicMock
from Backend import RestClient
import requests.exceptions


class BackendTestCases(unittest.TestCase):

    def setUp(self):
        self.client = RestClient.RestClient(url="testUrl")

    def test_post_valid(self):
        self.client.post = MagicMock(return_value="{valid_return:1}")
        response = self.client.post()
        self.assertEqual(response, "{valid_return:1}")

    def test_post_timeout(self):
        exception = requests.exceptions.Timeout()
        self.client.post = MagicMock(side_effect=exception)
        self.assertRaises(requests.exceptions.Timeout, self.client.post)

    def test_post_connection_error(self):
        exception = requests.exceptions.ConnectionError()
        self.client.post = MagicMock(side_effect=exception)
        self.assertRaises(requests.exceptions.ConnectionError, self.client.post)

    def test_post_invalid_url(self):
        exception = requests.exceptions.InvalidURL()
        self.client.post = MagicMock(side_effect=exception)
        self.assertRaises(requests.exceptions.InvalidURL, self.client.post)

    def test_get_valid(self):
        self.client.get = MagicMock(return_value="{valid_return:2}")
        response = self.client.get()
        self.assertEqual(response, "{valid_return:2}")

    def test_get_timeout(self):
        exception = requests.exceptions.Timeout()
        self.client.get = MagicMock(side_effect=exception)
        self.assertRaises(requests.exceptions.Timeout, self.client.get)

    def test_get_connection_error(self):
        exception = requests.exceptions.ConnectionError()
        self.client.get = MagicMock(side_effect=exception)
        self.assertRaises(requests.exceptions.ConnectionError, self.client.get)

    def test_get_invalid_url(self):
        exception = requests.exceptions.InvalidURL()
        self.client.get = MagicMock(side_effect=exception)
        self.assertRaises(requests.exceptions.InvalidURL, self.client.get)

    def tearDown(self):
        self.client = None

if __name__ == '__main__':
    unittest.main()
