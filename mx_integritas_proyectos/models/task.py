from odoo import _, api, fields, models, tools
from datetime import datetime, timedelta

class Task(models.Model):
    _name = 'project.task'
    _inherit = ['project.task']

    date_assign = fields.Datetime(string='Assigning Date', index=True, copy=False, readonly=False)
    date_now_gmt = fields.Datetime(string='Date Now', index=True, copy=False, readonly=False ,compute='_set_date_gtm')

    @api.multi
    def _set_date_gtm(self):
    	for dato in self:
    		date_gtm =  datetime.now() - timedelta(hours=6)
    		dato.date_now_gmt = date_gtm
        

