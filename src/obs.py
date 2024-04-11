import obsws_python as obs

# pass conn info if not in config.toml
client = obs.ReqClient()

version = client.get_version()

print(f'OBS Version: {version.obs_version}')


def start_record():
    record_status = client.get_record_status()
    if record_status.output_active:
        return

    client.start_record()


def stop_record():
    record_status = client.get_record_status()
    if not record_status.output_active:
        return

    client.stop_record()
