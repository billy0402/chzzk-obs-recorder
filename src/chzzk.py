from time import sleep

from python_chzzk import Chzzk, Credential
from python_chzzk.models import Channel, LiveStatus

from actions import start_streaming, stop_streaming
from models.cache import Cache
from obs import is_obs_recording
from settings import settings

cache: dict[str, Cache] = {}


def is_chzzk_changing_status(
    channel: Channel,
    live_status: LiveStatus,
) -> bool:
    return not cache.get(channel.channel_id) \
       or live_status.status != cache[channel.channel_id].live_status.status


async def main():
    credential = Credential(
        auth=settings.chzzk_auth,
        session=settings.chzzk_session,
    )
    chzzk = Chzzk(credential)

    channel_id = settings.chzzk_channel_id
    channel = await chzzk.channel(channel_id)
    live_status = await chzzk.live.status(channel_id=channel_id)

    if is_chzzk_changing_status(channel, live_status):
        if live_status.status == 'OPEN':
            start_streaming(channel, live_status)
        else:  # 'CLOSE'
            stop_streaming(channel, live_status)
    elif live_status.status == 'OPEN' and not is_obs_recording():
        start_streaming(channel, live_status)
    elif live_status.status == 'CLOSE' and is_obs_recording():
        stop_streaming(channel, live_status)

    channel_cache = Cache(channel=channel, live_status=live_status)
    cache[channel_id] = channel_cache


async def loop_main():
    while True:
        try:
            await main()
        except Exception as e:
            print(e)

        sleep(settings.time_delay)
