import asyncio
import sys

from actions import stop_recording
from chzzk import loop_main

try:
    asyncio.run(loop_main())
except (KeyboardInterrupt, asyncio.exceptions.CancelledError):
    stop_recording()
    sys.exit(130)
