from slasher.response import SlashResponse


def load_actions(module='actions'):
    """Provides an easy way to discover user-created Actions without requiring
    the user to explicitly import them or register them. By default, it will
    attempt to import the 'actions' module, though it can attempt to import
    any module passed in.

    Importing a module that contains a subclass of BaseAction will result in
    that subclass being added to the action registry.
    """
    try:
        __import__(module)
    except ImportError:
        pass


class ActionException(Exception):
    """Generic exception from the actions. Include a useful error message with
    the exception in order to catch and return the message to the user.
    """
    pass


class ActionMount(type):
    """Metaclass for the BaseAction class. It is used to enable easily hooking
    in additional actions that subclass BaseAction.

    Any subclass of BaseAction will have a 'registry' attribute that contains
    a dictionary of registered actions where the key is the 'action_name' for
    a class and the value is the class itself.
    """
    def __init__(cls, name, bases, attrs):
        if not hasattr(cls, 'registry'):
            cls.registry = {}
        else:
            cls.registry[cls.name()] = cls


class BaseAction(object):
    """The base class for an Action.

    All Action subclasses should:

    1) Set an 'action_name' attribute on the class. This will determine
    how your action is called from your slash command.

    2) Set the text in the 'help()' classmethod. This will provide helpful
    information to your users on what each action does.

    3) (Optionally) Set detailed help text in the `detailed_help()` classmethod.
    This is the text that will be returned if a user wants more specific help on
    a particular action. For complicated actions, it's good to give 2-3 lines of
    help as well as an example or two.

    4) Implement the 'run()' method. This is the method that will be executed
    when a particular action is called. If you're using the default Slasher
    handler for Lambda, you should return either a SlashResponse object (preferred),
    or a string of text to be displayed to the user. If there's an Exceeption,
    you should raise an ActionException with a message that describes the problem
    to the calling user.
    """

    __metaclass__ = ActionMount
    action_name = None

    def __init__(self, slash):
        self.slash = slash

    @classmethod
    def name(cls):
        if not cls.action_name:
            raise Exception("Give your action a name.")
        return cls.action_name

    @classmethod
    def help(cls):
        """Returns short help text to the user when asking for help on using
        your command.
        """
        raise NotImplementedError()

    @classmethod
    def detailed_help(cls):
        """A way to return more detailed help text on a particular command to
        a user. Useful for providing examples or describing in-depth options.

        If this is not implemented, it will return the help() text for the class.
        """
        return cls.help()

    def run(self):
        """The method that will be called when your action is invoked.
        """
        raise NotImplementedError()


class HelpAction(BaseAction):
    """Action for when a user calls the command with 'help'. Enables both
    general high-level help on all available commands, as well as detailed
    help on a specific command.

    Invocation examples:

    /slash help -- For requesting general help
    /slash help list -- For requesting detailed help on the 'list' action
    """

    action_name = 'help'

    @classmethod
    def help(cls):
        return """Show the options for this slash command. Use help <action> to show detailed help on an action."""

    def run(self):
        # If the text is one word or less, they just want general help.
        if len(self.slash.text_parts) < 2:
            values = '\n'.join(self.get_all_help_text())
            msg = ("Available commands:\n\n"
                   "{values}".format(values=values))
        # Calling `help <action>`, so find the action if it exists and return detailed help.
        else:
            detailed_action = self.slash.text_parts[1]
            if detailed_action in self.registry:
                msg = self.registry[detailed_action].detailed_help()
            else:
                raise ActionException('You requested detailed help on {action}, \
                                       but there is no action by that name.'.format(action=detailed_action))

        return SlashResponse.in_channel(msg)

    def get_all_help_text(self):
        return ['{action}\t-\t{help}'.format(action=action, help=cls.help())
                for action, cls in self.registry.iteritems()]
