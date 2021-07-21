# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import requests
import xml.etree.ElementTree as ET
from datetime import datetime
#from .libro_azul import LibroAzul

class Controllers(http.Controller):
    
    @http.route(['/a/b'], type='json', auth='public', methods=['POST'], website=True, csrf=False)
    def index_modelo(self, **post):
        return "Hola mundo"
