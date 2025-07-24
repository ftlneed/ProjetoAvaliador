import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()  # Carrega o arquivo .env

def conectar():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("root"),
        password=os.getenv("admin123"),
        database=os.getenv("loja.db")
    )
