import psycopg2

def get_connection():
    try:
        conn = psycopg2.connect(
            dbname="DB_PostgreSQL",
            user="admin",
            password="Fimbrethil!",
            host="localhost",
            port="5432"
        )
        return conn
    except Exception as e:
        print(f"Erro ao conectar ao banco: {e}")
        return None
