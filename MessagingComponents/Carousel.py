from MessagingComponents.Constants import FB_BUTTON_TITLE_CHARACTER_LIMIT, FB_BUTTON_LIMIT, FB_ELEMENTS_LIMIT, FB_QUICK_REPLY_LIMIT, FB_TITLE_CHARACTER_LIMIT, FB_PAYLOAD_CHARACTER_LIMIT

class CarouselWeb:

    def __init__(self):
        self.template = {
            "carousel": []
        }

    def add_element(self, image_url='', title='', caption='', buttons=None, default_action_url=''):
        payload = {'image_url': image_url, "title": title, "caption": caption, "buttons": buttons,
                   "default_url": default_action_url}
        self.template["carousel"].append(payload)

    def get_message(self):
        return self.template


class CarouselFB:
    def __init__(self):
        self.template = {
            'attachment': {
                'type': 'template',
                'payload': {
                    'template_type': 'generic',
                    'image_aspect_ratio': 'horizontal',
                    'elements': []
                }
            }
        }
        self.elements = []

    def set_image_aspect_ratio_to_square(self):
        self.template['attachment']['payload']['image_aspect_ratio'] = 'square'

    def add_element(self, title='', image_url='', subtitle='', default_action_url='', buttons=[],
                    messanger_extensions=True):
        element = {}
        element['title'] = title[:80]
        element['image_url'] = image_url
        if subtitle != '':
            element['subtitle'] = subtitle
        if default_action_url != '':
            default_action = {}
            default_action['type'] = 'web_url'
            default_action['url'] = default_action_url
            default_action['webview_height_ratio'] = 'tall'
            default_action['messenger_extensions'] = messanger_extensions
            element['default_action'] = default_action
        for button in buttons:
            button['title'] = button['title'][:FB_BUTTON_TITLE_CHARACTER_LIMIT]
        if len(buttons) > 0:
            element['buttons'] = buttons[:FB_BUTTON_LIMIT]
        if len(self.elements) < FB_ELEMENTS_LIMIT:
            self.elements.append(element)

    def get_message(self):
        self.template['attachment']['payload']['elements'] = self.elements
        return self.template
