import unittest

from slasher.decorators import slasher

from tests.helpers import TEST_EVENT, TEST_SLASH_COMMAND


@slasher
def lambda_example(event, context):
    """Sample lambda handler function that just returns the
    event that is passed in
    """
    return event


class TestSlasher(unittest.TestCase):

    def test_slasher_can_decorate_handler_function(self):

        event = TEST_EVENT

        result = lambda_example(event, '')

        self.assertTrue('slasher' in result)
        self.assertEqual(TEST_SLASH_COMMAND.__dict__, result['slasher'].__dict__)

    def test_slasher_raises_value_error_if_improper_event(self):

        event = {'notbody': 'badvalue'}

        with self.assertRaises(ValueError):
            lambda_example(event, '')
