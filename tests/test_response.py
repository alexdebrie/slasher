import unittest

from slasher.response import SlashResponse


class TestSlashResponse(unittest.TestCase):

    def test_respond_makes_valid_response(self):
        response = SlashResponse(text='test')

        expected = {
            'statusCode': 200,
            'body': '{"text": "test", "response_type": "in_channel"}'
        }

        self.assertEqual(response.respond(), expected)

    def test_in_channel_classmethod_uses_in_channel_response(self):
        response = SlashResponse.in_channel(text='test')

        expected = {
            'statusCode': 200,
            'body': '{"text": "test", "response_type": "in_channel"}'
        }

        self.assertEqual(response.respond(), expected)

    def test_ephemeral_classmethod_uses_ephemeral_response(self):
        response = SlashResponse.ephemeral(text='test')

        expected = {
            'statusCode': 200,
            'body': '{"text": "test", "response_type": "ephemeral"}'
        }

        self.assertEqual(response.respond(), expected)

    def test_invalid_response_type_raises_error(self):
        with self.assertRaises(ValueError):
            SlashResponse(text='test', response_type='radio')
