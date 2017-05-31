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

