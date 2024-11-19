from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from tkinter import messagebox




#Configurando a engine do DB
engine = create_engine("sqlite:///users.db")

Session = sessionmaker(engine)
session = Session()

#Criando a tabela
Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    user = Column(String, unique=True, nullable=False)
    senha = Column(String, nullable=False)



#Cria a db
Base.metadata.create_all(engine) 


    

