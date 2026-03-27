import pyodbc
import os

def get_connection():
    driver = "{ODBC Driver 17 for SQL Server}"
    server = os.environ.get('DB_SERVER')
    database = os.environ.get('DB_NAME')
    username = os.environ.get('DB_USER')
    password = os.environ.get('DB_PASSWORD')

    connection_string = f"DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}"
    
    try:
        conn = pyodbc.connect(connection_string)
        return conn
    except Exception as e:
        print(f"ERROR DE CONEXIÓN A SOMEE: {e}")
        raise e