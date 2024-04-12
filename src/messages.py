from python_chzzk.models import Channel, LiveStatus


def chzzk_start_streaming(channel: Channel) -> str:
    return f'[CHZZK] {channel.channel_name} is streaming.'


def chzzk_stop_streaming(channel: Channel) -> str:
    return f'[CHZZK] {channel.channel_name} stop streaming.'


def chzzk_live_message(channel: Channel, live_status: LiveStatus) -> str:
    return f'''\
title: {live_status.live_title}
url: https://chzzk.naver.com/live/{channel.channel_id}\
    '''


def obs_start_recording() -> str:
    return '[OBS] start recording'


def obs_stop_recording() -> str:
    return '[OBS] stop recording'
