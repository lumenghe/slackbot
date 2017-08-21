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


def reply_to_text(text, channel):
    """
    Receive @tellme message and update environment
    """
    global current_bot
    global active_bots
    reply, current_bot, active_bots = parse_message(text, current_bot, active_bots, chatservice_host)
    slack_client.api_call("chat.postMessage", channel=channel, text=reply, as_user=True)

def parse_slack_output(slack_rtm_output):
    """
    Return None unless the message startswith @tellme
    """
    output_list = slack_rtm_output
    if output_list and len(output_list) > 0:
        for output in output_list:
            if output and 'text' in output and output['text'].startswith("@tellme"):
                return output['text'], output['channel']
    return None, None

