from urlparse import parse_qsl


class SlashCommand(object):
    """Object for holding the information from an invoked Slash command."""

    def __init__(self, channel_id=None, channel_name=None, command=None,
                 text=None, response_url=None, team_domain=None, team_id=None,
                 token=None, user_id=None, user_name=None):

        self.channel_id = channel_id
        self.channel_name = channel_name
        self.command = command
        self.text = text
        self.text_parts = text.split(' ')
        self.response_url = response_url
        self.team_domain = team_domain
        self.team_id = team_id
        self.token = token
        self.user_id = user_id
        self.user_name = user_name

    @classmethod
    def from_querystring(cls, querystring):
        """A slash command invocation passes in its information as a
        application/x-www-form-urlencoded string. This class method will
        return an instance of SlashCommand built from a valid querystring.
        """
        params = {k: str(v) for k, v in parse_qsl(querystring)}
        return cls(**params)

    @property
    def requested_action(self):
        if self.text_parts:
            return self.text_parts[0]
        else:
            return ''
