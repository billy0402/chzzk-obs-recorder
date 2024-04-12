import requests

from settings import settings


def line_notify_api_notify(message: str):
    if not settings.line_notify_access_token:
        return

    headers = {
        'Authorization': f'Bearer {settings.line_notify_access_token}',
    }
    body = {
        'message': message,
    }
    return requests.post(
        'https://notify-api.line.me/api/notify',
        body,
        headers=headers,
    )
