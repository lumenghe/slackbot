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
