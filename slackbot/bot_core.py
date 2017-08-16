from six.moves import range
import requests
import socket


def get_bot_name(host, port, timeout=2):
    """
    Get name of chatbot service at host:port
    None if no such service exists there
    """
    s = socket.socket()
    socket.setdefaulttimeout(timeout)
    try:
        s = s.connect((host, port))
        rep = requests.get("http://{}:{}/getbotname".format(host, port), timeout=timeout)
        name = rep.json()["botname"]
        return name
    except:
        return None

def get_active_bots(host, min_num=5000, max_num=5100):
    """
    List active chatbot services on host
    """
    active = dict()
    for port in range(min_num, max_num):
        name = get_bot_name(host, port)
        if name is not None:
            active[name] = port
    return active

def parse_message(text, current_bot, active_bots, chatservice_host):
    """
    Parse @tellme messages, get reply and updated environment
    """
    reply = ""
    if text.startswith("@tellme "):
        question = text.split("@tellme ")[1].strip()
        if question.startswith("list"):
            active_bots = get_active_bots(chatservice_host)
            reply = "\n".join(["{}. {}".format(i+1, n) for i,n in enumerate(active_bots)])
            if reply == "":
                reply = "Nobody's there :-("
        elif question.startswith("start_session "):
            name = question.split("start_session ")[1].strip()
            if name in active_bots:
                if current_bot is not None and current_bot != name:
                    reply = "You switched from {} to {}".format(current_bot, name)
                else:
                    reply = "You are now chatting with {}".format(name)
                current_bot = name
            else:
                reply = "Nobody's called '{}' here. Why not asking who's there? ('@tellme list')".format(name)
        elif question.startswith('end_session'):
            reply = "You closed the session with {}".format(current_bot)
            current_bot = None
        elif current_bot is None:
            reply = "And nobody listened... Why not asking who's there? ('@tellme list')"
        else:
            try:
                rep = requests.get("http://{}:{}/askmeanything?q={}".format(chatservice_host, active_bots[current_bot], question))
                answer = rep.json()["response"]
                reply = "{}: {}".format(current_bot, answer)
            except:
                reply = "{} (speaking from the deads): I'm unreachable...".format(current_bot)
    return reply, current_bot, active_bots
