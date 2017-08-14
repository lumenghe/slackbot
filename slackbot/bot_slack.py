from __future__ import print_function
import os
import time
import argparse
from slackclient import SlackClient
from bot_core import parse_message


# websocket setting
READ_WEBSOCKET_DELAY = 1
# start Slack client
slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))
# environment vars
slackbot_host = None
chatservice_host = None
active_bots = dict()
current_bot = None

