class LocationWeb:

    def __init__(self, text=None):
        self.template = {
            "attachments": []
        }

    def add_element(self, type="location", sub_type="basic"):
        payload = {'type': type, 'sub_type': sub_type}
        self.template["attachments"].append(payload)

    def get_message(self):
        return self.template


