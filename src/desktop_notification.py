from pynotifier import Notification, NotificationClient
from pynotifier.backends import platform


def show_desktop_notification(title: str, message: str = ''):
    client = NotificationClient()
    client.register_backend(platform.Backend())
    notification = Notification(title=title, message=message)
    client.notify_all(notification)
