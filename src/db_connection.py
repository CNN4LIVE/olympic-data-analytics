import os
import urllib.parse
import pandas as pd
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "olympics_db")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASS = os.getenv("DB_PASS", "Xfiles77!")

def get_db_engine():
    safe_password = urllib.parse.quote_plus(DB_PASS)
    safe_user = urllib.parse.quote_plus(DB_USER)
    
    connection_string = f"postgresql+psycopg2://{safe_user}:{safe_password}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    
    engine = create_engine(
        connection_string,
        connect_args={
            'options': '-c client_encoding=utf8'
        }
    )
    return engine

def run_query(query: str) -> pd.DataFrame:
    engine = get_db_engine()
    with engine.connect() as conn:
        df = pd.read_sql_query(text(query), conn)
    return df

if __name__ == "__main__":
    try:
        test_df = run_query("SELECT 1 AS test_connection;")
        print("✅ Datenbankverbindung erfolgreich hergestellt!")
        print(test_df)
    except Exception as e:
        print("❌ Verbindung fehlgeschlagen. Prüfe Passwort/Datenbankname.")