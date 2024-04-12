# chzzk-obs-recorder

A Python script to start/stop recording when CHZZK channel start/stop streaming.

**Start recording**
![Start recording](/docs/images/start-recording.jpg)

**Stop recording**
![Stop recording](/docs/images/stop-recording.jpg)

## Development environment

- [macOS 12.7.2](https://www.apple.com/tw/macos/monterey/)
- [Visual Studio Code 1.85.1](https://code.visualstudio.com/)
- [Python 3.11.7](https://www.python.org/)
- [python-chzzk](https://github.com/billy0402/python-chzzk)
- [obsws-python](https://github.com/aatikturk/obsws-python)
- [py-notifier](https://github.com/YuriyLisovskiy/pynotifier)

## Installation

```shell
$ pip install -r requirements.txt
# or
$ pipenv install
```

## Setup environment variables

```shell
$ cp .env.example .env
```

| Variable                 | Type              | Default Value | Description                                             |
| ------------------------ | ----------------- | ------------- | ------------------------------------------------------- |
| TIME_DELAY               | Optional[Integer] | 10            | Time delay (in seconds) for checking the channel status |
| CHZZK_AUTH               | String            |               | NID_AUT of CHZZK                          |
| CHZZK_SESSION            | String            |               | NID_SES of CHZZK                                 |
| CHZZK_CHANNEL_ID         | String            |               | Channel ID of CHZZK                                     |
| LINE_NOTIFY_ACCESS_TOKEN | Optional[String]  |               | Access token for LINE Notify, or LINE Notify won't send |

You can retrieve `NID_AUT` and `NID_SES` from browser cookie using https://chzzk.naver.com after logging in.

You can obtain `access_token` from LINE Notify, the API document https://notify-bot.line.me/doc/en/.

## Setup OBS WebSocket

This project is using OBS WebSocket APIs to control OBS.

So you need to setup OBS WebSocket to allow the script to connect to OBS.

`obs-websocket` is now included by default with OBS Studio 28.0.0 and above.

If your OBS is not that new, please install it by yourself from [this link](https://github.com/obsproject/obs-websocket/releases).

![OBS WebSocket setup](/docs/images/obs-websocket.jpg)

Please update the connection information with `config.toml`.

More information: [obsws-python config file](https://github.com/aatikturk/obsws-python?tab=readme-ov-file#config-file).

## Setup OBS scene

You should set up OBS scene by yourself.

This script will only trigger the start and stop recording with OBS.

## Usage

```shell
$ cd <path-to-chzzk-obs-recorder>

$ python src/main.py
```

## Common Error

```shell
WNDPROC return value cannot be converted to LRESULT
TypeError: WPARAM is simple, so must be an int object (got NoneType)
```

This is a `win_toaster` issue, dependent on this issue: [Windows-10-Toast-Notifications issue](https://github.com/jithurjacob/Windows-10-Toast-Notifications/issues/112).

We won't change the package behavior.

If there is another solution to fix it, please let me know.

---

Ctrl + C may not stop the loop immediately.

Please try more times to stop the process.

If it still does not stop, please close the terminal.

And check if OBS has stopped recording.

## Bugs and suggestions

If you have found a bug or have a request for additional functionality, please use the issue tracker on GitHub.

https://github.com/billy0402/chzzk-obs-recorder/issues
