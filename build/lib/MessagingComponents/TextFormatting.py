from MessagingComponents.Constants import CHANNEL_NAME_FACEBOOK, CHANNEL_NAME_REST


def get_new_line_ready_text(channel: str, text: str) -> str:
    if channel == CHANNEL_NAME_REST:
        text = text.replace('/n', '<br>')
    if channel == CHANNEL_NAME_FACEBOOK:
        text = text.replace('/n ', '\n')
    return text