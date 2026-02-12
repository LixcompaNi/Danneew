import hashlib
import uuid
from flask import Flask, request, jsonify

app = Flask(__name__)

# Хэш пароля администратора (создается один раз)
ADMIN_KEY_HASH = hashlib.sha256("твой_секретный_пароль".encode()).hexdigest()

@app.route('/api/register', methods=['POST'])
def register_user():
    data = request.json
    # Генерация неизменяемого ID
    account_id = f"ANO-{uuid.uuid4().hex[:8].upper()}"
    
    # Формируем структуру данных пользователя
    user_data = {
        "id": account_id,
        "name": data.get("name"),
        "phone": data.get("phone"),
        "email": data.get("email"),
        "status": "active"
    }
    return jsonify({"message": "User created", "data": user_data})

@app.route('/api/admin/nuke', methods=['POST'])
def admin_nuke():
    # Проверка ключа доступа в заголовках
    client_key = request.headers.get("X-Admin-Auth")
    if not client_key or hashlib.sha256(client_key.encode()).hexdigest() != ADMIN_KEY_HASH:
        return "Not Found", 404
    
    target = request.json.get("target_id")
    return jsonify({"status": "Success", "action": f"Account {target} deleted forever"})

if __name__ == "__main__":
    app.run(debug=True)
