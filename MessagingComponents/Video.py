from MessagingComponents.Constants import FB_ELEMENTS_LIMIT


class VideoWeb:

    def __init__(self):
        self.template = {
            "attachments": []
        }

    def add_element(self, type="video", url=''):
        payload = {'type': type, 'url':url}
        self.template["attachments"].append(payload)

    def get_message(self):
        return self.template


class VideoFB:
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

    def add_element(self, media_type='video', attachment_id=''):
        element = {'media_type': media_type, 'attachment_id': attachment_id}
        if len(self.elements) < FB_ELEMENTS_LIMIT:
            self.elements.append(element)

    def get_message(self):
        self.template['attachment']['payload']['elements'] = self.elements
        return self.template