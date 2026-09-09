import os
from dotenv import load_dotenv

# Загружаем переменные из .env
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
EXCEL_PATH = os.getenv("EXCEL_PATH", "clients.xlsx")

# Проверка наличия обязательных ключей
if not BOT_TOKEN or not TELEGRAM_CHAT_ID:
    raise ValueError("Ошибка: BOT_TOKEN или TELEGRAM_CHAT_ID не заданы в файле .env!")