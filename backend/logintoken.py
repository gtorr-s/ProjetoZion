import jwt
import datetime

# Chave secreta para codifica��o do JWT (substitua por uma chave segura)
SECRET_KEY = "sua_chave_secreta"

def generate_login_token(user_id):
    """
    Gera um token JWT para autenticar o usu�rio.
    
    :param user_id: ID do usu�rio para incluir no token.
    :return: Token JWT como uma string.
    """
    payload = {
        "user_id": user_id,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)  # Expira em 1 hora
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return token
