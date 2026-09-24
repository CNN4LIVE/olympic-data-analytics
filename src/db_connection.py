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
DB_PASS = os.getenv("DB_PASSWORD") or os.getenv("DB_PASS", "XFiles77!")

def get_db_engine():
    safe_password = urllib.parse.quote_plus(DB_PASS)
    safe_user = urllib.parse.quote_plus(DB_USER)
    
    # sslmode=require ist zwingend für Neon.tech Cloud PostgreSQL
    url = f"postgresql://{safe_user}:{safe_password}@{DB_HOST}:{DB_PORT}/{DB_NAME}?sslmode=require"
    return create_engine(url)