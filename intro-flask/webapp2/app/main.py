#!/usr/bin/env python

#  Programa: main.py
# Propósito: Creación aplicación web Flask
#     Autor: Marius Lungu
#     Fecha: 31/12/2019 

import flask import Flask
import os

app = Flask(__name__)

#REDIS_LOCATION=os.environ.get("REDIS_LOCATION", None)
#REDIS_LOCATION=os.environ["REDIS_LOCATION"]

#PORT=os.environ.get("PORT",5000)
PORT=os.environ["PORT"]

@app.route('/hello')
def hello_world():
	Nombre=os.environ.get("NOMBRE","Sin nombre")
	return f"Ronaldinho, soy yo, el balon de oro de 2006, y mi mejor amigo es NOMBRE={NOMBRE}"

@app.route('/bye')
def bye_world():
	return ("Ronaldinho tendria que tener 2 balones de oro.")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=PORT)
