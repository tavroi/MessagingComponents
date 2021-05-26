import uuid


class FormWeb:

    def __init__(self, form_id:str):
        self.template = {
            "form": {
                "form_id": form_id,
                "fields": []
            }
        }

    def add_elements(self, element_type, label, name, value=""):
        payload = {
            "type": element_type,
            "label": label,
            "name": f"{name}",
            "id": f"{name}_{self.template['form']['form_id']}",
            "class": f"{name}_{self.template['form']['form_id']}",
            "value": value,
        }
        self.template["form"]["fields"].append(payload)

    def get_message(self):
        return self.template
