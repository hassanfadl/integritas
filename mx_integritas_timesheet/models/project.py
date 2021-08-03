#-*- coding: utf-8 -*-

from odoo import models, fields, api


class mx_integritas_timesheet(models.Model):
	_inherit = 'project.task'

	@api.depends('remaining_hours')
	def compute_function(self):
		if self.remaining_hours &lt; 0:
			return True
		else:
			return False
    	
	is_email_timesheet_send = fields.Boolean(string='Correo Parte de Horas')
	status_hours_exceded = fields.Boolean(compute=compute_function, string='Exceded hours')

