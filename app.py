import asyncio
import platform
from functools import wraps
from quart import jsonify, Quart, render_template, request, websocket
from quart_openapi import Resource

from resources.common import CustomLogger
#from resources import websocket

#from resources.ciscoaxl import *

# Definimos los parametros de logs
applog = CustomLogger.getCustomLogger('quartapp', 'QuartCiscoCollab','DEBUG')

# Definmos la aplicacion
app = Quart(__name__)

# Registramos todas las URL para Rest API

@app.route("/", methods=['GET', 'POST'])
async def index():
    applog.info ('Se esta utilizando Python v%s' % ( platform.python_version() ) )
    applog.debug ('Ha accedido a la pagina principal con el metodo: %s' % (request.method))
    return await render_template("customer.html")

@app.websocket('/')
async def ws(customer='CUSTOMER'):
    while True:
        data = await websocket.receive()
        applog.info ('Se esta utilizando Python v%s en Websocket' % ( platform.python_version() ) )
        applog.info ('Cliente: %s' % ( customer ) )
        await websocket.send(f"echo {data}")

# Ejecutamos la aplicación con certificado para HTTP/2
# sudo openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 730 -nodes
# curl --include --insecure --http2 https://127.0.0.1:8443/
@app.cli.command('run')
def run():
    app.run(host='127.0.0.1', port=8443, certfile='cert.pem', keyfile='key.pem')
    #app.run(host='127.0.0.1', port=8443)