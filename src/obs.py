import obsws_python as obs

from settings import settings

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
            print(f'OBS Version: {version.obs_version}')
            return True
    except ConnectionRefusedError:
        print('OBS is not activated.')
        return False


def get_obs_is_recording() -> bool:
    with OBSClient() as client:
        record_status = client.get_record_status()
        return record_status.output_active


def obs_start_recording():
    if not is_obs_opened():
        return

    with OBSClient() as client:
        record_status = client.get_record_status()
        if record_status.output_active:
            return

        client.start_record()


def obs_stop_recording():
    if not is_obs_opened():
        return

    with OBSClient() as client:
        record_status = client.get_record_status()
        if not record_status.output_active:
            return

        client.stop_record()
