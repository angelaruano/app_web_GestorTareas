from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

#engine : Permite a SQLAlchemy comunicarse con la base de datos.
engine = create_engine ("sqlite:///database/tareas.db",connect_args={"check_same_thread": False})
#Advertencia : Crear engine no conecta directamente con la base de datos, Eso se hace más adelante.

#sesión : Crear la sesión nos permite hacer transacciones (operaciones) en la BD.
Session = sessionmaker(bind = engine)
session = Session()

#vinculación: Es donde convertimos las clases en tablas
# En models, tenemos que decir qué clase queremos convertir en tabla, pegando la siguiente variable.
#Así se mapean las clases que hay que convertir. Se lo ponemos en la herencia:
#class Persona (Base)
Base = declarative_base()