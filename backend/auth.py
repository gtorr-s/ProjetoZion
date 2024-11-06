import hashlib
import secrets
import jwt
from datetime import datetime, timedelta

SECRET_KEY = '3DHNPCFJEFWEZJ'

def generate_login_token(username):
    return hashlib.sha256(username.encode()).hexdigest()

def generate_password():
    return secrets.token_urlsafe(12)

def generate_login_token(user_id):
    expiration = datetime.utcnow() + timedelta(minutes=5) # Token válido por 5 minutos
    token = jwt.encode({'user_id': user_id, 'exp': expiration}, SECRET_KEY, algorithms='HS256')
    return token

