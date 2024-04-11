import requests


def line_notify_api_notify(access_token: str, message: str):
    headers = {
        'Authorization': f'Bearer {access_token}',
    }
    body = {
        'message': message,
    }
    return requests.post(
        'https://notify-api.line.me/api/notify',
        body,
        headers=headers,
    )
