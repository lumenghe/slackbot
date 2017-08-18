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


@app.route('/askfromcli', methods=['GET'])
def ask_from_cli():
    """
    Receive text from CLI interface
    """
    global current_bot
    global active_bots
    text = request.args.get('q')
    reply, current_bot, active_bots = parse_message(text, current_bot, active_bots, chatservice_host)
    return jsonify({'response': reply})

@app.route("/")
def home():
    return "CLI Slackbot is running here :-)"

