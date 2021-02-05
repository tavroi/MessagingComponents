from MessagingComponents.QuickReply import QuickReplyWeb, QuickReplyFB
from MessagingComponents.Carousel import CarouselWeb, CarouselFB
from MessagingComponents.Button import ButtonTemplateFB
from MessagingComponents.Constants import CHANNEL_NAME_FACEBOOK, CHANNEL_NAME_REST
from MessagingComponents.TextFormatting import get_new_line_ready_text


def create_quick_replies(channel: str, text: str, quick_reply_data: dict) -> dict:
    if channel == CHANNEL_NAME_REST:
        qrw = QuickReplyWeb(
            get_text_formatted_for_different_channels(channel, text))
        for item in quick_reply_data:
            if item["action_type"] == "postback":
                qrw.add_generic_(
                    type=item["action_type"], title=item["title"], payload=item["payload"], user_input=item.get("user_input", True))
            else:
                qrw.add_generic_(
                    type=item["action_type"], title=item["title"], web_url=item["web_url"], user_input=item.get("user_input", True), extension=False)
        return qrw.get_message()

    elif channel == CHANNEL_NAME_FACEBOOK:
        qrfb = QuickReplyFB(
            get_text_formatted_for_different_channels(channel, text))
        for item in quick_reply_data:
            qrfb.add_quick_reply(
                content_type="text", title=item["title"], payload=item["payload"], image_url=item.get("image_url", None))
        return qrfb.get_message()


def create_carousel(channel, carousel_data):
    if channel == CHANNEL_NAME_REST:
        crw = CarouselWeb()
        for card in carousel_data:
            buttons = []
            for button in card["button"]:
                buttons.append(
                    {"type": button["type"], "url": button["url"], "title": button["title"], "extension": button.get("messanger_extensions", True)})
            crw.add_element(image_url=card["image_url"], title=card["title"], default_action_url=card.get("default", ""),
                            buttons=card["button"],
                            caption=card["caption"]
                            )
        return crw.get_message()

    elif channel == CHANNEL_NAME_FACEBOOK:
        crfb = CarouselFB()
        for card in carousel_data:
            buttons = []
            for button in card["button"]:
                buttons.append({"type": button["type"], "url": button["url"], "title": button["title"],
                                "webview_height_ratio": "full", "messanger_extensions": button.get("messanger_extensions", True)})
            crfb.add_element(title=card["title"], subtitle=card["caption"],
                             image_url=card["image_url"],
                             buttons=card["button"], messanger_extensions=card["button"]["messanger_extensions"])
        return crfb.get_message()


def create_buttons(channel: str, text: str, buttons_data: dict) -> dict:
    if channel == CHANNEL_NAME_REST:
        for index in range(len(buttons_data)):
            buttons_data[index]["web_url"] = buttons_data[index]["url"]
            buttons_data[index]["action_type"] = "web_url"
        return create_quick_replies(channel, get_text_formatted_for_different_channels(channel, text), buttons_data)
    elif channel == CHANNEL_NAME_FACEBOOK:
        bfb = ButtonTemplateFB(
            get_text_formatted_for_different_channels(channel, text))
        for button in buttons_data:
            bfb.add_web_url(title=button["title"], url=button["url"])
            return bfb.get_message()


def get_text_formatted_for_different_channels(channel: str, text: str) -> str:
    text = get_new_line_ready_text(channel, text)
    return text
