from typing import Optional

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    time_delay: int = 10

    chzzk_auth: str
    chzzk_session: str
    chzzk_channel_id: str

    obs_websocket_host: str = 'localhost'
    obs_websocket_port: int = 4455
    obs_websocket_password: str = ''
    obs_websocket_timeout: int = 3

    line_notify_access_token: Optional[str] = None

    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
    )


settings = Settings()
