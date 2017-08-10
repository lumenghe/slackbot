import argparse
from flask import Flask, request, jsonify
from bot_core import parse_message


# start flask app
app = Flask(__name__)
# environment vars
slackbot_host = None
chatservice_host = None
active_bots = dict()
current_bot = None

