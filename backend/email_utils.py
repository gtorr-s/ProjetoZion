import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_login_email(user_email, link):
    sender_email = "kingfirecraft@gmail.com"
    sender_password = "Fimbrethil1409!"

    message = MIMEMultipart("alternative")
    message["subject"] = "Seu link de Login"
    message["From"] = sender_email
    message["To"] = user_email

    text = f"Olá! Clique no link para acessar sua conta: {link}. Este link é válido por apenas 5 minutos."
    message.attach(MIMEText(text, "plan"))

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, sender_password)
            server.sendemail(sender_email, user_email, message.as_string())
        print("E-mail enviado com sucesso!")
    except Exception as e:
        print(f"Erro ao enviar o e-mail: {e}")