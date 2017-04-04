import copy
import unittest

from slasher.actions import BaseAction, HelpAction, load_actions
from tests.helpers import TEST_SLASH_COMMAND


class TestActionRegistry(unittest.TestCase):

    def test_help_action_in_registry(self):
        expected = {'help': HelpAction}

        self.assertEqual(BaseAction.registry, expected)

    def test_load_action(self):

        self.assertEqual(len(BaseAction.registry), 1)

        load_actions('tests.fake_action')

        self.assertEqual(len(BaseAction.registry), 2)
        self.assertIn('fake', BaseAction.registry)


class TestHelpAction(unittest.TestCase):

    def test_returns_general_help_with_no_text(self):
        slash = copy.copy(TEST_SLASH_COMMAND)
        slash.text = ''

        expected = """\
Available commands:

help\t-\tShow the options for this slash command. Use help <action> to show detailed help on an action.
fake\t-\tUsed for helping test actions."""

        action = HelpAction(slash)
        text_result = action.run().text

        self.assertEqual(text_result, expected)
