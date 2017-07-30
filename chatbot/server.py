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

