from sqlalchemy import Column, Integer, String, Text, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Tworzymy bazę do deklaracji modeli
Base = declarative_base()

# Definicja klasy Ksiazka
class Mebel(Base):
    __tablename__ = 'Meble'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nazwa = Column(String, nullable=False)
    cena = Column(Integer, nullable=True)
    kupione = Column(Boolean, nullable = True)

    def __repr__(self):
        return f"<Mebel(id={self.id}, nazwa='{self.nazwa}', cena='{self.cena}, kupione='{self.kupione}'')>"