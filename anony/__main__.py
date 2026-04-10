import asyncio
import importlib
import os
from flask import Flask
from threading import Thread

from pyrogram import idle

from anony import app, db, logger
from anony.modules import all_modules


# 🔹 Flask setup
flask_app = Flask(__name__)

@flask_app.route('/')
def home():
    return "Bot is running!"

def run():
    flask_app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))

def keep_alive():
    t = Thread(target=run)
    t.start()


async def anony_boot():
    try:
        await app._start()
    except Exception as ex:
        raise RuntimeError(ex)
    await db.connect()

    for module in all_modules:
        importlib.import_module(f"anony.modules.{module}")
    logger.info(f"Loaded {len(all_modules)} modules.")

    await idle()
    await app._stop()
    await db.close()


if __name__ == "__main__":
    keep_alive()  # 🔥 Flask start
    asyncio.get_event_loop().run_until_complete(anony_boot())
    logger.info("Stopping String Gen Bot...")
