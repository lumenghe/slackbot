FROM python:3.4

WORKDIR app/

# Install required python libs
ADD requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

# Copy code from current folder to /app in container
ADD . app/

# Make port 5001 available
EXPOSE 5001

#CMD python bot_cli.py --chatservice_host 0.0.0.0 --slackbot_host 0.0.0.0 --port 5001 ; python bot_slack.py --chatservice_host 0.0.0.0
