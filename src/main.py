import asyncio
import sys

from chzzk import main
from desktop_notification import show_desktop_notification
from line_notification import line_notify_api_notify
from obs import stop_record

while True:
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        stop_record()
        show_desktop_notification(title='[OBS] stop record')
        line_notify_api_notify(message='[OBS] stop record')
        sys.exit(130)
