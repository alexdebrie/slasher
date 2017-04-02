import json

VALID_RESPONSE_TYPES = ['in_channel', 'ephemeral']


class SlashResponse(object):
    """An object for responding to a Slash command invocation.

    To initialize, call with the text you would like to respond with:

    resp = SlashResponse(text='Thanks for invoking my slash command!')

    You may also specify a response type ("in_channel" (default) or "ephemeral"):

    resp = SlashResponse(text='Shh, don't tell anyone', response_type='ephemeral')

    You can use the in_channel() and ephemeral() classmethods for your desired
    response type:

    loud = SlashResponse.in_channel(text='This is an in channel response')
    quiet = SlashResponse.ephemeral(text='This is an ephemeral response')

    Finally, use the respond() method to actually respond to the Slash command:

    def lambda_handler(event, context):
        response = handle(event) # Do some work and return a SlashResponse object.

        return response.respond() # Send the response back
    """

    def __init__(self, text, response_type='in_channel'):

        self.text = text
        if response_type not in VALID_RESPONSE_TYPES:
            raise ValueError('Invalid response type of {}. Must be one of {}'.format(
                response_type, VALID_RESPONSE_TYPES))
        else:
            self.response_type = response_type

    @classmethod
    def in_channel(cls, text):
        return cls(text=text, response_type='in_channel')

    @classmethod
    def ephemeral(cls, text):
        return cls(text=text, response_type='ephemeral')

    def respond(self):
        return {
            'statusCode': 200,
            'body': json.dumps({
                'text': self.text,
                'response_type': self.response_type
            })
        }
