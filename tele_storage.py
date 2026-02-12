import requests

TOKEN = "8425879350:AAFGD4ciCaBKW5ZeKLwgddLOIS4N4-dwPBQ"
CHAT_ID = "-1002242062534" # Твой канал t.me/+fW1WSB8ahMFhM2Uy

def send_to_storage(json_payload):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    
    # Форматируем JSON для удобного чтения в Telegram
    text_message = f"📦 **NEW DATA STORAGE**\n\n```json\n{json_payload}\n```"
    
    payload = {
        "chat_id": CHAT_ID,
        "text": text_message,
        "parse_mode": "MarkdownV2"
    }
    
    response = requests.post(url, json=payload)
    return response.status_code == 200

# Пример использования:
# send_to_storage({"id": "ANO-123", "action": "LOGIN"})
