from python_chzzk.models import Channel, LiveStatus


def start_title(channel: Channel):
    return f'[CHZZK] {channel.channel_name} is streaming.'


def stop_title(channel: Channel):
    return f'[CHZZK] {channel.channel_name} stop streaming.'


def channel_message(channel_id: str, live_status: LiveStatus):
    return f'''\
title: {live_status.live_title}
url: https://chzzk.naver.com/live/{channel_id}\
            '''
