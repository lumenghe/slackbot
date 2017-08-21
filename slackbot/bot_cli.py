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


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='CLI interface to communicate with slackbot')
    parser.add_argument('--chatservice_host', help='host for chatbot service(s)', type=str, default="0.0.0.0")
    parser.add_argument('--slackbot_host', help='host for slackbot', type=str, default="0.0.0.0")
    parser.add_argument('-p','--port', help='port for slackbot', type=int, required=True)
    args = parser.parse_args()
    chatservice_host = args.chatservice_host
    slackbot_host = args.slackbot_host
    port = args.port
    app.run(debug=True, host=slackbot_host, port=port)
