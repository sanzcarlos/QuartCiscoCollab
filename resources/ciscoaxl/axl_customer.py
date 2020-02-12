from lib import CustomLogger
from quart.logging import default_handler
from quart import Blueprint, render_template

applog = CustomLogger.getCustomLogger('rest_axl_customer', 'quartapp')

rest_axl_customer = Blueprint ('rest_axl_customer',__name__)

@rest_axl_customer.route ('/api/v1/axl/<customer>/<devicename>', methods = ['GET'])
async def rest_axl_customer_get(customer,devicename):
    applog.info ('The Customer is: ' + customer + ' and the Device Name is: ' + devicename)
    return await render_template('customer.html', name = customer + devicename)
