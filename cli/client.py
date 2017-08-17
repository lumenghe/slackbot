from __future__ import print_function
from six.moves import input
import requests
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='CLI interface to communicate with slackbot')
    parser.add_argument('--host', help='host for slackbot', type=str, default="0.0.0.0")
    parser.add_argument('-p','--port', help='port for slackbot', type=int, required=True)
    args = parser.parse_args()
    host = args.host
    port = args.port
    try:
        while True: # user interaction loop
            question = input("> ")
            try:
                rep = requests.get("http://{}:{}/askfromcli?q={}".format(host, port, question))
                answer = rep.json()["response"]
                print(answer.strip())
            except:
                print("ClientError: communication with slackbot service failed!")
    except (KeyboardInterrupt, EOFError, SystemExit):
        print("\nBye!")
