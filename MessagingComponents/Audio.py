class AudioWeb:

    def __init__(self):
        self.template = {
            "attachments": []
        }

    def add_element(self, type="audio", url=''):
        payload = {'type': type, 'url':url}
        self.template["attachments"].append(payload)

    def get_message(self):
        return self.template