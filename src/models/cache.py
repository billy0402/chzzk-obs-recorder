from pydantic import BaseModel
from python_chzzk.models import Channel, LiveStatus


class Cache(BaseModel):
    channel: Channel
    live_status: LiveStatus
