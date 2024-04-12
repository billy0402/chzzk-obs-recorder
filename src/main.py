import asyncio
import sys

from actions import stop_recording
from chzzk import main

while True:
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, asyncio.exceptions.CancelledError):
        stop_recording()
        sys.exit(130)
