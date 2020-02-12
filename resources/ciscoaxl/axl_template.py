# -*- coding: iso-8859-15 -*-

# *------------------------------------------------------------------
# * axl_template.py
# *
# * Cisco AXL Python
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

# Import Modules
from lib import CustomLogger
from quart.logging import default_handler
from quart import Blueprint, render_template

applog = CustomLogger.getCustomLogger('rest_axl_template', 'quartapp')

rest_axl_template = Blueprint ('rest_axl_template',__name__)

@rest_axl_template.route ('/api/v1/axl/<customer>/<devicename>', methods = ['GET'])
async def rest_axl_template_get(customer,devicename):
    applog.info ('The Customer is: ' + customer + ' and the Device Name is: ' + devicename)
    return await render_template('customer.html', name = customer + devicename)

from flask_restful import Resource
from flask import Flask, render_template, request, jsonify
from flask_restful import Resource, Api
from quart.logging import default_handler
from quart import Blueprint, render_template, request, jsonify
from lxml import etree
from common import CustomLogger, CustomSoap

import os
import sys
import json
import zeep
import logging
import asyncio

class CiscoAXL_Template(Resource):