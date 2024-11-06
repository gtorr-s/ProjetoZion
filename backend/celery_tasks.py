#backend/celery_tasks.py

from celery import Celery
from datetime import datetime, timedelta
import db_config
import secrets

app = Celery('tasks', broker='redis://redis:6379/0', backend='redis://redis:6379/0')

@app.task
def update_passwords():
    conn = db_config.get_connection()
    with conn.cursor() as cursor:
        new_password = secrets.token_urlsafe(12)
        now = datetime.now()
        query = """
        UPDATE clientes
        SET password = %s, password_last_updated = %s
        WHERE password_lst_updated <= %s;
        """

        cursor.execute(query, (new_password, now, now - timedelta(hours=6)))
        conn.commit()
        conn.close()
