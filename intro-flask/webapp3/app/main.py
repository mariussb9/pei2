#!/usr/bin/env python

#  Programa: main.py
# Propósito: Creación aplicación web Flask
#     Autor: Óscar García
#     Fecha: 09/12/2019 

import flask


# Crear el objeto que representa la aplicacion web
APP = flask.Flask(__name__)


@APP.route('/')
def index():
	user_info = { "username": "Marius", "visit_counter": 9 }
	return flask.render_template('index.html',info=user_info)


if __name__ == '__main__':
    APP.debug = True
    APP.run(host='0.0.0.0', port=5000)
