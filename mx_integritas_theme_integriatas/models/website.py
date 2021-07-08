# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from odoo.exceptions import Warning
import datetime
import logging
_logger = logging.getLogger(__name__)

class Website(models.Model):
	_inherit = 'website'
	text_whatsapp = fields.Char( string="Whats App Text",help="Insert text whatsapp")    