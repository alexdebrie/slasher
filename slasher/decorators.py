from functools import wraps

from slasher.command import SlashCommand


def slasher(f):
    """slasher is a decorator for Lambda handler functions. It pulls the 'body'
    key from the Lambda event argument, builds a SlashCommand object, and adds
    the SlashCommand object to the event. The altered event and context are then
    passed into the Lambda handler function.
    """
    @wraps(f)
    def wrapper(event, context):
        body = event.get('body')
        if not body:
            raise ValueError("Event object must have a 'body' key.")

        s = SlashCommand.from_querystring(body)
        event['slasher'] = s
        return f(event, context)
    return wrapper
