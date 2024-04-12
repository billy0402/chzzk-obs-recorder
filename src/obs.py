import obsws_python as obs


def is_obs_opened() -> bool:
    try:
        # pass conn info if not in config.toml
        with obs.ReqClient() as client:
            version = client.get_version()
            print(f'OBS Version: {version.obs_version}')
            return True
    except ConnectionRefusedError:
        print('OBS is not activated.')
        return False


def start_record():
    if not is_obs_opened():
        return

    with obs.ReqClient() as client:
        record_status = client.get_record_status()
        if record_status.output_active:
            return

        client.start_record()


def stop_record():
    if not is_obs_opened():
        return

    with obs.ReqClient() as client:
        record_status = client.get_record_status()
        if not record_status.output_active:
            return

        client.stop_record()
