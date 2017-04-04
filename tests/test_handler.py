import copy
import unittest

from slasher.handler import lambda_handler
from tests.helpers import TEST_EVENT


class TestLambdaHandler(unittest.TestCase):

    def test_valid_lambda_handler_returns_valid_response(self):
        event = copy.deepcopy(TEST_EVENT)
        result = lambda_handler(event, 'blee')

        self.assertEqual(result['statusCode'], 200)
        self.assertIn('Available commands', result['body'])
