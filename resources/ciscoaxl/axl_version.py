from lib import CustomLogger
from quart.logging import default_handler
from quart import Blueprint, render_template

applog = CustomLogger.getCustomLogger('rest_axl_version', 'quartapp')

rest_axl_version = Blueprint ('rest_axl_version',__name__)

@rest_axl_version.route ('/api/v1/axl_version/', methods = ['GET'])
async def rest_axl_version_get():
    #axl_version.logger.debug ('Request method %s' % request.method)
    applog.info ('Request method')
    return await render_template('index.html', name = 'Blueprint - AXL Version - GET')

@rest_axl_version.route ('/api/v1/axl_version/', methods = ['DELETE'])
async def rest_axl_version_delete():
    return await render_template('index.html', name = 'Blueprint - AXL Version - DELETE')

@rest_axl_version.route ('/api/v1/axl_version/', methods = ['PUT'])
async def rest_axl_version_put():
    return await render_template('index.html', name = 'Blueprint - AXL Version - PUT')
