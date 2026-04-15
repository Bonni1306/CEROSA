import os
import pyodbc
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    # Construcción de la cadena de conexión
    conn_str = (
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={os.getenv('DB_HOST')};"
        f"DATABASE={os.getenv('DB_NAME')};"
        f"UID={os.getenv('DB_USER')};"
        f"PWD={os.getenv('DB_PASS')};"
        "TrustServerCertificate=yes;"
    )
    
    try:
        conn = pyodbc.connect(conn_str)
        return conn
    except Exception as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None