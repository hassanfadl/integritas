#-*- coding: utf-8 -*-

from odoo import models, fields, api


class mx_integritas_timesheet(models.Model):
	_inherit = 'project.task'

	@api.depends('remaining_hours')
	def compute_function(self):
		for record in self:
			if record.remaining_hours < 0:
				record.status_hours_exceded = True
			else:
				record.status_hours_exceded = False
    	
	is_email_timesheet_send = fields.Boolean(string='Correo Parte de Horas')
	status_hours_exceded = fields.Boolean(compute=compute_function, string='Exceded hours')