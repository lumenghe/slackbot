Slackbot task
==============

I designed a chatbot architecture to run bot services independently and interacting with them through a Command Line Interface (CLI) or Slack. The code is compatible with both Python 2 and 3.

Note: debugger is activated for flask to help evaluation.

Features
--------------

* Run multiple chatbot services on a host
* A single client for interface with user
* The client adapts dynamically to the number of running bot services
* The client is robust to bot service failures

Architecture
--------------

The code has three main modules:
* `chatbot` for running chatbot services
* `slackbot` for running the client service, which communicate on CLI or Slack
* `cli` for running the CLI

Python requirements
--------------

The following Python modules are used in my code

* argparse
* chatterbot
* flask
* requests
* six
* slackclient
* socket (already in the standard library)


Usage (manually)
--------------

I give the commands for testing locally each part of the code. Provided the requirements are installed, the first thing is to start chatbot services, for example:

```
python chatbot/server.py --name "Wall-E" --host 0.0.0.0 --port 5002 --bot English --workdir /tmp/
python chatbot/server.py --name "HAL 9000" --host 0.0.0.0 --port 5003 --bot Math --workdir /tmp/
```
Name, host IP and port, and bot type (English, Zen or Math) are required. More services can be started on different ports.

The second step is to run the slackbot service, which will scan the ports to find running bots. This version interacts with CLI:

```
python slackbot/bot_cli.py --chatservice_host 0.0.0.0 --slackbot_host 0.0.0.0 --port 5001
```

It searches for bot services on a single host (here: *localhost*), and runs as a web service on provided host and port.

The other option is to run a Slack service, which requires to [set up a Slackbot account](https://www.fullstackpython.com/blog/build-first-slack-bot-python.html). The Slack token is passed to Python using the environment variable `SLACK_BOT_TOKEN`. 
```
export SLACK_BOT_TOKEN=************************ (change to your slack bot token)
python slackbot/bot_slack.py --chatservice_host 0.0.0.0
```

In addition, if we run the CLI service, we can send commands using:

```
python cli/client.py --host 0.0.0.0 --port 5001
```

After all the services are started, we can type *@tellme* commands in CLI or Slack to interact with the bots:

* *@tellme list*: for listing available bots
* *@tellme start_session name_of_the_bot*: to begin chatting with a bot 
* *@tellme end_session*: to terminate a chat with a bot

Usage (with Docker)
--------------

We create docker images to run the different services presented above. The three modules have requirements and Dockerfile for building containers. We can use Docker-compose to build and run the complete service suite:

```
docker-compose up --build
```

Then it is possible to send messages from Slack or the CLI. Bots are configured to create their databases at /tmp/.

Possible improvements
--------------

I can think of some improvements for this code, which could be done with a longer timeline:

1. For the moment the code doesn't have automated tests, everything was checked manually.
2. Port scanning for searching bot services can be slow, it could be multithreaded.
3. Dynamic discovery of bot services could be extended to many host. That would be done differently: bots would register to a central service which would ping them regularly to update the list.

