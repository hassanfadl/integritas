from odoo import _, api, fields, models, tools, pytz, datetime


class Task(models.Model):
    _name = 'project.task'
    _inherit = ['project.task']

    date_assign = fields.Datetime(string='Assigning Date', index=True, copy=False, readonly=False)
    date_now_gmt = fields.Datetime(string='Date Now', index=True, copy=False, readonly=False ,compute='_set_date_gtm')

    @api.multi
    def _set_date_gtm(self):
    	for stock in self:
    		stock.date_now_gmt = datetime.datetime.now()
        

