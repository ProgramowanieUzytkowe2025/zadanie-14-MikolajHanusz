from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.modelMebel import Base
import urllib.parse

params = urllib.parse.quote_plus(
    "DRIVER=ODBC Driver 17 for SQL Server;"
    "SERVER=(localdb)\\MSSQLLocalDB;"
    "DATABASE=Ikea;"
    "Trusted_Connection=yes;"
)

SQLALCHEMY_DATABASE_URL = f"mssql+pyodbc:///?odbc_connect={params}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Tworzymy silnik bazy danych
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Tworzymy sesję
SessionLocal = sessionmaker(bind=engine)

# Funkcja do tworzenia bazy danych
def init_db():
    Base.metadata.create_all(bind=engine)