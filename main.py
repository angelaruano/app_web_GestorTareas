from flask import Flask, render_template, request, redirect, url_for
import db
from models import Tarea

app = Flask(__name__) #Aquí está el servidor web

#La barra (slash) es la ruta de la página de inicio
#Justo debajo, en def home() le estamos diciendo el comportamiento a seguir.
#Ésta es, pues, la vinculación entre python y mi navegdor.
@app.route("/")
def home():
    todas_las_tareas = db.session.query(Tarea).all()
    for x in todas_las_tareas:
        print(x)
    return render_template("index.html",lista_de_tareas = todas_las_tareas) #Conexión de html con el main.

#En la siguiente línea, hago la ruta para que desde html se invoque a la función y se envíe el input.
@app.route("/crear-tarea", methods=["POST"])
def crear():
    #Con request.form, le estoy preguntando al formulario de html "contenido_tarea", su contenido.
    tarea = Tarea(contenido=request.form["contenido_tarea"], categoria=request.form["categoria_tarea"],fecha_limite=request.form["fecha_limite_tarea"],hecha=False)
    db.session.add(tarea)
    db.session.commit()
    return redirect(url_for("home"))

@app.route("/editar-tarea/<id>", methods=["POST"])
def editar(id):
    tarea = db.session.query(Tarea).filter_by(id_tarea = id).first()
    tarea.contenido = request.form["new_contenido_tarea"]
    tarea.categoria = request.form["new_categoria_tarea"]
    tarea.fecha_limite = request.form["new_fecha_limite_tarea"]
    db.session.commit()
    return redirect(url_for("home"))


#La siguiente función servirá para que cuando quiera eliminar una tarea, html y python se vinculen a través de jinja2 y dicha tarea se elimine.
@app.route("/eliminar-tarea/<id>") #Estoy creando la ruta y poniendo <id> estoy indicando que hay un contenido.
def eliminar(id):
    tarea = db.session.query(Tarea).filter_by(id_tarea=id)
    tarea.delete()
    db.session.commit()
    return redirect(url_for("home"))

@app.route("/tarea-hecha/<id>")
def hecha(id):
    tarea = db.session.query(Tarea).filter_by(id_tarea=id).first()
    tarea.hecha = not (tarea.hecha)
    db.session.commit()
    return redirect(url_for("home"))

if __name__ == "__main__":
    db.Base.metadata.create_all(db.engine)
    app.run(debug = True) #Ésto arranca el servidor (lo crea y lo activa)