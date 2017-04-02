from slasher.command import SlashCommand

TEST_EVENT = {u'body': u'token=TestToken1234&team_id=T111A1A11&team_domain=test&channel_id=A1A11AAAA&channel_name=privategroup&user_id=A1A1AA1A6&user_name=testuser&command=%2Ftestslash&text=testing&response_url=https%3A%2F%2Fhooks.slack.com%2Fcommands%2FA111A1111%2F111111111113%2Fa1zAAa11AAAaAAaA1aaaAaAa'}

TEST_SLASH_COMMAND = SlashCommand(
    token='TestToken1234',
    team_id='T111A1A11',
    team_domain='test',
    channel_id='A1A11AAAA',
    channel_name='privategroup',
    user_id='A1A1AA1A6',
    user_name='testuser',
    command='/testslash',
    text='testing',
    response_url='https://hooks.slack.com/commands/A111A1111/111111111113/a1zAAa11AAAaAAaA1aaaAaAa'
)
