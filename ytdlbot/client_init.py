

from pyrogram import Client

from config import APP_HASH, APP_ID, PYRO_WORKERS, TOKEN, WORKERS, IPv6


def create_app(name: str, workers: int = PYRO_WORKERS) -> Client:
    return Client(
        name,
        APP_ID,
        APP_HASH,
        bot_token=TOKEN,
        workers=workers,
        ipv6=IPv6,
        max_concurrent_transmissions=max(1, WORKERS // 2),
        # https://github.com/pyrogram/pyrogram/issues/1225#issuecomment-1446595489
    )
