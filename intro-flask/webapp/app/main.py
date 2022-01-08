#!/usr/bin/env python

#  Programa: main.py
# Propósito: Creación aplicación web Flask
#     Autor: Marius Florin Lungu
#     Fecha: 09/12/2019 

import flask
import socket
import redis
import os

#REDIS_LOCATION=os.environ.get("REDIS_LOCATION", None)
#REDIS_LOCATION=os.environ["REDIS_LOCATION"]

# Crear el objeto que representa la aplicacion web
APP = flask.Flask(__name__)
redis_cli = redis.Redis(host='redisserver', port=6379, db=0)

@APP.route('/')
def index():
    userinfo = {
        "username": "Marius",
	#"visit_counter": 1234
    }

    # num_visitas = num_visitas + 1 
    redis_cli.incr('num_visitas')
    num_visitas = redis_cli.get('num_visitas')
    hostname = socket.gethostname()
    return flask.render_template('index.html',
				 visit_counter=num_visitas.decode("utf-8"),
				 info=userinfo,
				 server_name=hostname)
    
@APP.route('/reset')
def reset():
    redis_cli.set('num_visitas', 0)
    return ""

if __name__ == '__main__':
    APP.debug = True
    APP.run(host='0.0.0.0', port=5000)
