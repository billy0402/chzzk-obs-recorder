import asyncio

from python_chzzk import Chzzk, Credential

from env import chzzk_auth, chzzk_channel_id, chzzk_session


async def main():
    credential = Credential(auth=chzzk_auth, session=chzzk_session)
    chzzk = Chzzk(credential)

    channel_id = chzzk_channel_id
    live_status = await chzzk.live.status(channel_id=channel_id)
    print(live_status.status)


if __name__ == "__main__":
    asyncio.run(main())
