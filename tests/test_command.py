import unittest

from slasher.command import SlashCommand
from tests.helpers import TEST_EVENT, TEST_SLASH_COMMAND


class TestSlashCommand(unittest.TestCase):

    def test_can_parse_from_querystring(self):
        event = TEST_EVENT
        expected = TEST_SLASH_COMMAND

        result = SlashCommand.from_querystring(event['body'])

        self.assertEqual(expected.__dict__, result.__dict__)
