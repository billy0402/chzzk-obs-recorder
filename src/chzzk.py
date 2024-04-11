import asyncio

from python_chzzk import Chzzk, Credential

from desktop_notification import show_desktop_notification
from env import chzzk_auth, chzzk_channel_id, chzzk_session
from notification import channel_message, start_title, stop_title


async def main():
    credential = Credential(auth=chzzk_auth, session=chzzk_session)
    chzzk = Chzzk(credential)

    channel_id = chzzk_channel_id
    channel = await chzzk.channel(channel_id)
    live_status = await chzzk.live.status(channel_id=channel_id)

    if live_status.status == 'OPEN':
        show_desktop_notification(
            title=start_title(channel),
            message=channel_message(channel_id, live_status),
        )
    else:
        show_desktop_notification(
            title=stop_title(channel),
            message=channel_message(channel_id, live_status),
        )


if __name__ == "__main__":
    asyncio.run(main())
