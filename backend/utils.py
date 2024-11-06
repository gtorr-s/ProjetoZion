import secrets
import string
import time

# Armazena a senha e o tempo da última geração
senha_atual = None
ultima_geracao = 0

def generate_random_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for i in range(length))
    return password

def get_current_password():
    global senha_atual, ultima_geracao
    if time.time() - ultima_geracao >= 21600:  # 6 horas
        senha_atual = generate_random_password()
        ultima_geracao = time.time()
    return senha_atual

def authenticate_user(email, senha_fornecida, email_armazenado):
    if email != email_armazenado:
        return False
    senha_correta = get_current_password()
    return senha_fornecida == senha_correta
