from python_chzzk.models import Channel, LiveStatus

import messages
from desktop_notification import show_desktop_notification
from line_notification import line_notify_api_notify
from obs import obs_start_recording, obs_stop_recording


def stop_recording():
    obs_stop_recording()
    show_desktop_notification(title=messages.obs_stop_recording())
    line_notify_api_notify(message=messages.obs_stop_recording())


def start_streaming(channel: Channel, live_status: LiveStatus):
    show_desktop_notification(
        title=messages.chzzk_start_streaming(channel),
        message=messages.chzzk_live_message(channel, live_status),
    )
    line_notify_api_notify(message=f'''\
{messages.chzzk_start_streaming(channel)}

{messages.chzzk_live_message(channel, live_status)}\
    ''')

    obs_start_recording()
    show_desktop_notification(title=messages.obs_start_recording())
    line_notify_api_notify(message=messages.obs_start_recording())


def stop_streaming(channel: Channel, live_status: LiveStatus):
    show_desktop_notification(
        title=messages.chzzk_stop_streaming(channel),
        message=messages.chzzk_live_message(channel, live_status),
    )
    line_notify_api_notify(message=f'''\
{messages.chzzk_stop_streaming(channel)}

{messages.chzzk_live_message(channel, live_status)}\
    ''')

    stop_recording()
