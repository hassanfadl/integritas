# -*- coding: utf-8 -*-
from odoo import http
from odoo import http
from odoo.http import request
import requests
import xml.etree.ElementTree as ET
from datetime import datetime
class ControllerMassMailing(http.Controller):
    @http.route(['/save/addEmail'], type='http', auth='none', website=True, methods=['POST'], csrf=False)
    def api_rest(self, **post):
        #_logger.warning("Input Integritas")
        print("Francias turrentin")
        

        return str("hola")
