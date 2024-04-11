import os

from dotenv import load_dotenv

load_dotenv()

chzzk_auth = os.getenv('CHZZK_AUTH')
chzzk_session = os.getenv('CHZZK_SESSION')
chzzk_channel_id = os.getenv('CHZZK_CHANNEL_ID')
