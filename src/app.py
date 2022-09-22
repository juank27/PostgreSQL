from flask import Flask, render_template, url_for, flash, request, redirect
from config import *

app = Flask(__name__)
app.secret_key = 'mysecretkey' # para poder usar flash


con_db = get_connection()

#ruta de la pagina principal
@app.route("/")
def index():
	print(con_db)
	cur = con_db.cursor()
	cur.execute("SELECT * FROM personas")
	data = cur.fetchall()
	print("----------------------------------------------")
	print(data)
	return render_template("index.html", personas=data)
	#return render_template("index.html")

#ruta de layaut
@app.route("/layaut")
def layaut():
	print("Hola layut")
	return render_template("layout.html")

@app.route("/guardar_persona", methods=['POST'])
def guardar_personas():
	if request.method == 'POST':
		nombre = request.form['nombre']
		apellido = request.form['apellido']
		edad = request.form['edad']
		cur = con_db.cursor()
		cur.execute("INSERT INTO personas (nombre, apellido, edad) VALUES (%s, %s, %s)", (nombre, apellido, edad))
		con_db.commit()
		cur.execute("SELECT * FROM personas")
		data = cur.fetchall()
		print("----------------------------------------------")
		print(data)
		return render_template("index.html", personas=data)
		#return redirect(url_for('index'))

@app.route("/listar_personas")
def listar_personas():
	cur = con_db.cursor()
	cur.execute("SELECT * FROM personas")
	data = cur.fetchall()
	print(data)
	return render_template("ver.html", personas=data)

#Actualizar persona
@app.route("/update/<id>", methods=['POST'])
def get_persona(id):
	nombre = request.form['nombre']
	apellido = request.form['apellido']
	edad = request.form['edad']
	cur = con_db.cursor()
	if nombre and apellido and edad:
		sql = """
			UPDATE personas
			SET nombre = %s,
			apellido = %s,
			edad = %s
			WHERE id = %s
		"""
		cur.execute(sql, (nombre, apellido, edad, id))
		con_db.commit()
		flash("Persona actualizada correctamente", "success")
		return redirect(url_for('index'))
	else:
		return 'Error en la consulta'

#eliminar persona
@app.route("/delete/<id>")
def delete_persona(id):
	cur = con_db.cursor()
	cur.execute("DELETE FROM personas WHERE id=%s", (id))
	con_db.commit()
	return redirect(url_for('index'))

#ruta de error 404
@app.errorhandler(404)
def page_not_found(error):
   return render_template('404.html'), 404

# funciones
def create_table():
	cur = con_db.cursor()
	cur.execute("""
			CREATE TABLE IF NOT EXISTS personas(
				id serial  NOT NULL,
				nombre VARCHAR(50),
				apellido VARCHAR(50),
				edad INTEGER,
				CONSTRAINT pk_personas_id PRIMARY KEY (id));
		""")
	con_db.commit()

if __name__ == '__main__':
	create_table()
	app.run(debug=True, port=5000)