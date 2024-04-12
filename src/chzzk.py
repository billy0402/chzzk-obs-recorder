from time import sleep

from python_chzzk import Chzzk, Credential

from desktop_notification import show_desktop_notification
from line_notification import line_notify_api_notify
from models.cache import Cache
from notification import channel_message, start_title, stop_title
from obs import start_record, stop_record
from settings import settings

cache: dict[str, Cache] = {}


async def main():
    credential = Credential(
        auth=settings.chzzk_auth,
        session=settings.chzzk_session,
    )
    chzzk = Chzzk(credential)

    channel_id = settings.chzzk_channel_id
    channel = await chzzk.channel(channel_id)
    live_status = await chzzk.live.status(channel_id=channel_id)

    if not cache.get(channel_id)\
       or live_status.status != cache[channel_id].live_status.status:
        if live_status.status == 'OPEN':
            show_desktop_notification(
                title=start_title(channel),
                message=channel_message(channel_id, live_status),
            )
            line_notify_api_notify(message=start_title(channel) + '\n\n' +
                                   channel_message(channel_id, live_status))

            start_record()
            show_desktop_notification(title='[OBS] start record', message='')
            line_notify_api_notify(message='[OBS] start record')
        else:  # 'CLOSE'
            show_desktop_notification(
                title=stop_title(channel),
                message=channel_message(channel_id, live_status),
            )
            line_notify_api_notify(message=start_title(channel) + '\n\n' +
                                   channel_message(channel_id, live_status))

            stop_record()
            show_desktop_notification(title='[OBS] stop record', message='')
            line_notify_api_notify(message='[OBS] stop record')

    channel_cache = Cache(channel=channel, live_status=live_status)
    cache[channel_id] = channel_cache

    sleep(settings.time_delay)
