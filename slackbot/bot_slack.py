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


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='CLI interface to communicate with slackbot')
    parser.add_argument('--chatservice_host', help='host for chatbot service(s)', type=str, default="0.0.0.0")
    args = parser.parse_args()
    chatservice_host = args.chatservice_host
    if slack_client.rtm_connect():
        print("Slackbot is connected")
        try:
            while True:
                text, channel = parse_slack_output(slack_client.rtm_read())
                if text and channel:
                    reply_to_text(text, channel)
                time.sleep(READ_WEBSOCKET_DELAY)
        except (KeyboardInterrupt, EOFError, SystemExit):
            print("Slackbot terminated.")
    else:
        print("Connection failed. Please check connection or Slack token...")
