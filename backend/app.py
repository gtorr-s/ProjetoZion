from flask import Flask, request, jsonify
from utils import authenticate_user, get_current_password
import time

app = Flask(__name__)

# Email da empresa (pode ser armazenado em um banco de dados para múltiplos usuários)
email_armazenado = "kingcraft@gmail.com"

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get("email")
    senha = data.get("senha")
    
    if authenticate_user(email, senha, email_armazenado):
        return jsonify({"message": "Login bem-sucedido"}), 200
    else:
        return jsonify({"error": "Email ou senha incorretos"}), 401

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
