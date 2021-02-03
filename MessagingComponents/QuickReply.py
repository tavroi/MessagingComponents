from MessagingComponents.Constants import FB_BUTTON_TITLE_CHARACTER_LIMIT, FB_BUTTON_LIMIT, FB_ELEMENTS_LIMIT, FB_QUICK_REPLY_LIMIT, FB_TITLE_CHARACTER_LIMIT, FB_PAYLOAD_CHARACTER_LIMIT


class QuickReplyWeb:

    def __init__(self, text=None):
        self.template = {
            "quick_reply": {
                "text": text,
                "buttons": []
            },
            "input": True
        }

    def add_postback(self, title='', payload='', user_input=True):
        self.template["quick_reply"]["buttons"].append(
            {'title': title, 'type': 'postback', 'payload': payload})
        self.template["input"] = user_input

    def add_web_url(self, title='', url='', user_input=False, extension=False):
        self.template["quick_reply"]["buttons"].append(
            {'title': title, 'type': 'web_url', 'url': url, 'extension': extension})
        self.template["input"] = user_input

    def add_generic_(self, type, title, payload=None, web_url=None, text=None, user_input=True, extension=True):
        if type == "web_url":
            button = {'title': title, 'type': 'web_url',
                      'url': web_url, 'extension': extension}
        else:
            button = {'title': title, 'type': 'postback', 'payload': payload}
        self.template["quick_reply"]["buttons"].append(button)
        self.template["input"] = user_input

    def get_message(self):
        return self.template

class QuickReplyFB:

    def __init__(self, text):
        self.template = {"quick_replies": [], "text": text}

    def add_quick_reply(self, content_type="text", title="", payload="", image_url=None):
        if len(self.template["quick_replies"]) < FB_QUICK_REPLY_LIMIT:
            quick_reply_button = {"content_type": content_type,
                                  "title": title[:FB_BUTTON_TITLE_CHARACTER_LIMIT], 
                                  "payload": payload[:FB_PAYLOAD_CHARACTER_LIMIT]}
            if image_url is not None:
                quick_reply_button["image_url"] = image_url
            self.template["quick_replies"].append(quick_reply_button)

    def get_message(self):
        return self.template
