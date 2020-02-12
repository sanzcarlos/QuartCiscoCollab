# -*- coding: iso-8859-15 -*-

# *------------------------------------------------------------------
# * websocket.py
# *
# * WebSocket Server
# *
# * Copyright (C) 2020 Carlos Sanz <carlos.sanzpenas@gmail.com>
# *
# *  This program is free software; you can redistribute it and/or
# * modify it under the terms of the GNU General Public License
# * as published by the Free Software Foundation; either version 2
# * of the License, or (at your option) any later version.
# *
# *  This program is distributed in the hope that it will be useful,
# * but WITHOUT ANY WARRANTY; without even the implied warranty of
# * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# * GNU General Public License for more details.
# *
# *  You should have received a copy of the GNU General Public License
# * along with this program; if not, write to the Free Software
# * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301,
# *------------------------------------------------------------------
# *

# Modules
import asyncio
from functools import wraps
from quart import Blueprint, jsonify, Quart, render_template, request, websocket
from quart.logging import default_handler
from quart_openapi import Resource
from resources.common import CustomLogger

applog = CustomLogger.getCustomLogger('rest_websocket', 'QuartCiscoCollab')

rest_websocket = Blueprint ('rest_websocket',__name__)

# HTTP
@rest_websocket.route ('/ws/<customer>/<devicename>', methods = ['GET'])
async def rest_axl_customer_get(customer,devicename):
    applog.info ('The Customer is: ' + customer + ' and the Device Name is: ' + devicename)
    return await render_template('customer.html', name = customer + devicename)

# Websocket
@rest_websocket.websocket('/ws/<customer>/<devicename>')
async def ws(customer='null',devicename='null'):
    while True:
        data = await websocket.receive()
        applog.info ('customer: %s' % ( customer ) )
        applog.info ('devicename: %s' % ( devicename ) )
        await websocket.send(f"echo {data}")
