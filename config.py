from os import getenv
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = getenv("BOT_TOKEN")
MONGO_URL = getenv("MONGO_URL")

OWNER_ID = int(getenv("OWNER_ID", 7892805795))
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/log_channel_a")
