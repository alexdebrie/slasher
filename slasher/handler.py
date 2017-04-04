from slasher.actions import load_actions, BaseAction, ActionException
from slasher.decorators import slasher
from slasher.response import SlashResponse


@slasher
def lambda_handler(event, context):
    """A pretty simple lambda handler that should work for a lot of basic use
    cases. Based on the text of the Slash command, it tries to get a corresponding
    registered action and returns a message to the calling command.
    """
    slash = event['slasher']

    action = get_action(slash)

    # Avoid displaying an ugly error message to the user. If the action raises
    # an exception, we'll first try to use the message from an ActionException,
    # which should be helpful text on why the action failed. If a different
    # exception is raised, we'll fall back to a more generic error message.
    try:
        msg = action.run()
    except ActionException as e:
        msg = e.message
    except Exception as e:
        print e
        msg = "An error occurred. Bug the person who created this command."

    if not isinstance(msg, SlashResponse):
        msg = SlashResponse.in_channel(msg)

    return msg.respond()


def get_action(slash):
    """Searches for the applicable action and returns an instance of the
    action class with the given SlashCommand.

    When looking for the right action, it matches the 'requested_action'
    from the SlashCommand with the 'action_name' of registered actions.
    If there is no match, it returns the standard HelpAction.
    """
    load_actions()

    if slash.requested_action in BaseAction.registry:
        action_cls = BaseAction.registry[slash.requested_action]
    else:
        action_cls = BaseAction.registry['help']

    return action_cls(slash)
