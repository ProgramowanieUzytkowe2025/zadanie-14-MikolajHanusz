import requests
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from modelMebel import Mebel, Base
import urllib.parse

def main():
    # Baza danych

    params = urllib.parse.quote_plus(
    "DRIVER=ODBC Driver 17 for SQL Server;"
    "SERVER=(localdb)\\MSSQLLocalDB;"
    "DATABASE=Ikea;"
    "Trusted_Connection=yes;"
    )

    SQLALCHEMY_DATABASE_URL = f"mssql+pyodbc:///?odbc_connect={params}"
    engine = create_engine(SQLALCHEMY_DATABASE_URL)

    Session = sessionmaker(bind=engine)
    session = Session()


    nowy_mebel = Mebel(
        nazwa = "Arhuis",
        cena = 12.55,
        kupione = False
    )
    #session.add(nowy_mebel)
    #session.commit()
    print(session.query(Mebel).all())


if __name__ == "__main__":
    main()