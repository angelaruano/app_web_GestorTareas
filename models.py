from sqlalchemy import Column, Integer, String,Boolean
import db

class Tarea(db.Base):
    __tablename__ = "tarea"
    __table_args__ = {"sqlite_autoincrement": True}  # Automáticamente la PK de la tabla se va incrementando.
    id_tarea = Column(Integer, primary_key=True)
    contenido = Column(String(200), nullable=False)  # Ésto hace que el campo no pueda estar vacío
    categoria = Column(String(200))
    fecha_limite = Column(String(200))
    hecha = Column(Boolean)

    def __init__(self, contenido, categoria, fecha_limite, hecha):
        self.contenido = contenido
        self.categoria = categoria
        self.fecha_limite = fecha_limite
        self.hecha = hecha

    def __str__(self):
        return "Tarea: {} -> {} -> {} -> {} -> {}".format(self.id_tarea, self.contenido,self.categoria,self.fecha_limite, self.hecha)
