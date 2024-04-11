from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    chzzk_auth: str
    chzzk_session: str
    chzzk_channel_id: str

    line_notify_access_token: str

    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
    )
