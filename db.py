import pyodbc

def get_connection():
    conn = pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=Consultorio1.mssql.somee.com,1433;"
        "DATABASE=Consultorio1;"
        "UID=EdwinA180605_SQLLogin_2;"
        "PWD=vrnv83posc;"
        "Encrypt=yes;"
        "TrustServerCertificate=yes;"
    )
    return conn