from odoo import _, api, fields, models, tools

class Task(models.Model):
    _name = 'project.task'
    _inherit = ['project.task']

    date_assign = fields.Datetime(string='Assigning Date', index=True, copy=False, readonly=False)

