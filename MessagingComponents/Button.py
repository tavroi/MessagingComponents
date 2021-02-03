from MessagingComponents.Constants import FB_BUTTON_TITLE_CHARACTER_LIMIT, FB_BUTTON_LIMIT


class ButtonTemplateFB:
    def __init__(self, text=''):
        self.template = {
            'attachment': {
                'type': 'template',
                'payload': {
                    'template_type': 'button',
                    'text': text,
                    'buttons': []
                }
            }
        }
        self.text = text

    def add_web_url(self, title='', url='', messenger_extensions=True):
        if self.template['attachment']['payload']['buttons'] < FB_BUTTON_LIMIT:
            self.template['attachment']['payload']['buttons'].append({'type': 'web_url', 'url': url, 'title': title[:FB_BUTTON_TITLE_CHARACTER_LIMIT], 'messenger_extensions': messenger_extensions,
                                                                      'webview_height_ratio': 'tall'})

    def add_postback(self, title='', payload=''):
        self.template['attachment']['payload']['buttons'].append(
            {"type": "postback", "title": title, "payload": payload})

    def get_message(self):
        return self.template
