import psycopg2
import os

def get_connection():
    return psycopg2.connect(
        os.environ.get("postgresql://pacientes_db_ai2q_user:ENXCtNyxjxiMPYg6Ubo6ShqRUaJQksgq@dpg-d6uf45a4d50c73crmg4g-a.oregon-postgres.render.com/pacientes_db_ai2q")
    )


def get_connection():
    print("URL:", os.environ.get("DATABASE_URL"))
    return psycopg2.connect(os.environ.get("DATABASE_URL"))