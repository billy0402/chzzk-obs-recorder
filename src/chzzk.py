from time import sleep

from python_chzzk import Chzzk, Credential

from actions import start_streaming, stop_streaming
from models.cache import Cache
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
            start_streaming(channel, live_status)
        else:  # 'CLOSE'
            stop_streaming(channel, live_status)

    channel_cache = Cache(channel=channel, live_status=live_status)
    cache[channel_id] = channel_cache

    sleep(settings.time_delay)


async def loop_main():
    while True:
        await main()
