import os
import json
from flask import Flask, render_template,abort
app = Flask(__name__)	

with open("books.json") as fichero:
    datos=json.load(fichero)

@app.route('/',methods=["GET","POST"])
def inicio():
	return render_template("inicio.html",libros=datos)

@app.route('/libro/<isbn>',methods=["GET","POST"])
def libros(isbn):
	return render_template("libros.html",libros=datos)

app.run(debug=False)