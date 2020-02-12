from lib import CustomLogger
from quart.logging import default_handler
from quart import Blueprint, render_template

from AXL import *

applog = CustomLogger.getCustomLogger('rest_axl_phone', 'quartapp')

rest_axl_phone = Blueprint ('rest_axl_phone',__name__)

@rest_axl_phone.route ('/api/v1/axl_phone/', methods = ['GET'])
async def rest_axl_phone_get():
    applog.info ('Request method')
    return await render_template('index.html', name = 'Blueprint - AXL Phone - GET')

@rest_axl_phone.route ('/api/v1/axl_phone/', methods = ['DELETE'])
async def rest_axl_phone_delete():
    return await render_template('index.html', name = 'Blueprint - AXL Phone - DELETE')

@rest_axl_phone.route ('/api/v1/axl_phone/', methods = ['PUT'])
async def rest_axl_phone_put():
    return await render_template('index.html', name = 'Blueprint - AXL Phone - PUT')
