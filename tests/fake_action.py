from slasher.actions import BaseAction


class FakeAction(BaseAction):

    action_name = 'fake'

    @classmethod
    def help(self):
        return "Used for helping test actions."
