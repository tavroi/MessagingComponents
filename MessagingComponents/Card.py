class CardWeb:
    def __init__(self, image_url='', card_title=None, caption=None, card_url=''):
        self.template = {
            "card": {
                'image_url': image_url,
                'card_title': card_title,
                'caption': caption,
                'buttons': [],
                'card_url': card_url
            }
        }

    def add_element(self, title='', url=''):
        self.template["card"]["buttons"].append(
            {'title': title, 'type': 'web_url', 'url': url})

    def get_message(self):
        return self.template