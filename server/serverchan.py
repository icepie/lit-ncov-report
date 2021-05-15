import requests

class ServerChan(object):
    def __init__(self, sckey=""):
        self.url = "https://sc.ftqq.com/{}.send".format(sckey)

    def send(self, title, content=""):
        requests.get(self.url, params={"text": title, "desp": content})

class ServerChanTurbo(object):
    def __init__(self, sckey=""):
        self.url = "https://sct.ftqq.com/{}.send".format(sckey)

    def send(self, title, content=""):
        requests.get(self.url, params={"text": title, "desp": content})
