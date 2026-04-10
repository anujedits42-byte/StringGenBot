from os import getenv
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = getenv("BOT_TOKEN", "8676646717:AAGfnpz2tjYoTqrJMi5Dv0yX33_ZJGqbKfc")
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://Anujedit:Anujedit@cluster0.7cs2nhd.mongodb.net/?appName=Cluster0")
OWNER_ID = int(getenv("OWNER_ID",7892805795))
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/log_channel_a")
