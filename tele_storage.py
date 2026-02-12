import os
from dotenv import load_dotenv
import requests

# Загружаем переменные из файла .env
load_dotenv()

# Теперь токен берется из скрытой переменной
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = "-1002242062534"

def send_to_storage(json_payload):
    if not TOKEN:
        print("Ошибка: Токен не найден!")
        return
    
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    # ... остальной код функции ...
