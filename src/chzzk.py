import asyncio
from time import sleep

from python_chzzk import Chzzk, Credential

from desktop_notification import show_desktop_notification
from line_notification import line_notify_api_notify
from models.cache import Cache
from notification import channel_message, start_title, stop_title
from settings import Settings

settings = Settings()

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
            line_notify_api_notify(
                access_token=settings.line_notify_access_token,
                message=start_title(channel) + '\n\n' +
                channel_message(channel_id, live_status),
            )
        else:
            show_desktop_notification(
                title=stop_title(channel),
                message=channel_message(channel_id, live_status),
            )
            line_notify_api_notify(
                access_token=settings.line_notify_access_token,
                message=start_title(channel) + '\n\n' +
                channel_message(channel_id, live_status),
            )

    channel_cache = Cache(channel=channel, live_status=live_status)
    cache[channel_id] = channel_cache

    sleep(settings.time_delay)


if __name__ == "__main__":
    while True:
        asyncio.run(main())
