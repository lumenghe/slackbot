from __future__ import print_function
import argparse, os
from flask import Flask, request, jsonify
from bots import load_chatbot


#start flask app
app = Flask(__name__)
# environment vars
name = None
host = None
port = None
chatbot = None


@app.route('/askmeanything', methods=['GET'])
def chatquery():
    question = request.args.get('q')
    answer = chatbot.get_response(question).text
    return jsonify({'response': answer})

@app.route('/getbotname', methods=['GET'])
def getbotname():
    return jsonify({'botname': name})

@app.route("/")
def home():
    return "{} chatbot is running here :-)".format(name)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Chatbot arguments')
    parser.add_argument('-n','--name', help='name of the chatbot', type=str, required=True)
    parser.add_argument('--host', help='host for chatbot', type=str, default="0.0.0.0")
    parser.add_argument('-p','--port', help='port for chatbot', type=int, required=True)
    parser.add_argument('-b', '--bot', help='bot (English,Zen, or Math)', type=str, required=True)
    parser.add_argument('-w', '--workdir', help='work directory', type=str, default=os.getcwd())
    args = parser.parse_args()
    name = args.name
    host = args.host
    port = args.port
    botname = args.bot
    workdir = args.workdir
    print("Initializing chabot... ", end="")
    chatbot = load_chatbot(botname, name, port, workdir)
    print("done.")
    app.run(debug=True, host=host,port=port)