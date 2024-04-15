import obsws_python as obs

from settings import settings
from utils.logger import get_logger

logger = get_logger()

OBS_SOCKET_CONNECTION = {
    'host': settings.obs_websocket_host,
    'port': settings.obs_websocket_port,
    'password': settings.obs_websocket_password,
    'timeout': settings.obs_websocket_timeout,
}


class OBSClient(obs.ReqClient):

    def __init__(self):
        super().__init__(**OBS_SOCKET_CONNECTION)


def is_obs_opened() -> bool:
    try:
        with OBSClient() as client:
            version = client.get_version()
            logger.info(f'OBS Version: {version.obs_version}')
            return True
    except ConnectionRefusedError:
        logger.error('OBS is not activated.')
        return False


def on_obs_opened(func):

    def wrapper():
        if not is_obs_opened():
            return
        func()

    return wrapper


@on_obs_opened
def is_obs_recording() -> bool:
    with OBSClient() as client:
        record_status = client.get_record_status()
        return record_status.output_active


@on_obs_opened
def obs_start_recording():
    if is_obs_recording():
        return

    with OBSClient() as client:
        client.start_record()


@on_obs_opened
def obs_stop_recording():
    if not is_obs_recording():
        return

    with OBSClient() as client:
        client.stop_record()
