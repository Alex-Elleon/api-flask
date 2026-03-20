import psycopg2
import os

def get_connection():
    print("URL:", os.environ.get("DATABASE_URL"))
    return psycopg2.connect(os.environ.get("DATABASE_URL"))