import asyncio
import sys

from chzzk import main
from desktop_notification import show_desktop_notification
from line_notification import line_notify_api_notify
from obs import stop_record
from settings import settings

while True:
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        stop_record()
        show_desktop_notification(title='[OBS] stop record', message='')
        line_notify_api_notify(
            access_token=settings.line_notify_access_token,
            message='[OBS] stop record',
        )
        sys.exit(130)
