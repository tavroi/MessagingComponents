from MessagingComponents.Constants import FB_BUTTON_TITLE_CHARACTER_LIMIT, FB_BUTTON_LIMIT, FB_ELEMENTS_LIMIT, FB_QUICK_REPLY_LIMIT, FB_TITLE_CHARACTER_LIMIT, FB_PAYLOAD_CHARACTER_LIMIT

class ImageWeb:

    def __init__(self):
        self.template = {
            "attachments": []
        }

    def add_element(self, type="image", url=''):
        payload = {'type': type, 'url':url}
        self.template["attachments"].append(payload)

    def get_message(self):
        return self.template


class ImageFB:
    def __init__(self):
        self.template = {
            'attachment': {
                'type': 'template',
                'payload': {
                    'template_type': 'media',
                    'elements': [],
                    'sharable': 'false'
                }
            }
        }
        self.elements = []

    def add_element(self, media_type='image', attachment_id=''):
        element = {'media_type': media_type, 'attachment_id': attachment_id}
        if len(self.elements) < FB_ELEMENTS_LIMIT:
            self.elements.append(element)

    def get_message(self):
        self.template['attachment']['payload']['elements'] = self.elements
        return self.template