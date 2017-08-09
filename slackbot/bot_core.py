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
