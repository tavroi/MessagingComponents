import json
from Utills.ControlFile import FACEBOOK_BASE_URL, FACEBOOK_ACCESS_TOKEN
import requests


def upload_media_to_facebook(type: str, media_url: str):
    try:
        fb_url = f"{FACEBOOK_BASE_URL}me/message_attachments?access_token={FACEBOOK_ACCESS_TOKEN}"
        data = {
            "message": {
                "attachment": {
                    "type": type,
                    "payload": {
                        "is_reusable": True,
                        "url": media_url
                    }}
            }
        }
        response = requests.post(url=fb_url, json=data)

        print(response.text)
        # out_file = open("file.json", "w")
        # response_dict = json.loads(response.text)
        # json.dump(response_dict, out_file, indent=6)
        # out_file.close()

        return True, response.json(), "data found"
    except Exception as e:
        return False, {}, f"{e}"
