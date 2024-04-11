import asyncio

from python_chzzk import Chzzk, Credential

from desktop_notification import show_desktop_notification
from line_notification import line_notify_api_notify
from notification import channel_message, start_title, stop_title
from settings import Settings

settings = Settings()


async def main():
    credential = Credential(
        auth=settings.chzzk_auth,
        session=settings.chzzk_session,
    )
    chzzk = Chzzk(credential)

    channel_id = settings.chzzk_channel_id
    channel = await chzzk.channel(channel_id)
    live_status = await chzzk.live.status(channel_id=channel_id)

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


if __name__ == "__main__":
    asyncio.run(main())
