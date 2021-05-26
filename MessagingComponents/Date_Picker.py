class DatePickerWeb:

    def __init__(self):
        self.template = {
            "attachments": {
                "type": "calendar"
            }
        }

    def get_message(self):
        return self.template
