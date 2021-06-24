# -*- coding: utf-8 -*-

from odoo import api, fields, models

class ResCompany(models.Model):
    _inherit = 'res.partner'
    client_vip = fields.Boolean(string='Cliente Website', help="Selecciona par que el cliente aparezca en la página web")
    