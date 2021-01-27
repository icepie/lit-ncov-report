import requests

class CQHTTP(object):
    def __init__(self, url=""):
        self.url = url

    def send_group_msg(self, group_id: int, message: str, auto_escape: bool = True):
        data = {
            "group_id": group_id,
            "message": message,
            "auto_escape": auto_escape,
        }

        try:
            response = requests.post(
                url=self.url + "/send_group_msg", data=data
            )
            print(response.text)
        except:
            return None

        res = response.json()

        return res