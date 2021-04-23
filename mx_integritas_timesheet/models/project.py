#-*- coding: utf-8 -*-

from odoo import models, fields, api


class mx_integritas_timesheet(models.Model):
	_inherit = 'project.task'

	is_email_timesheet_send = fields.Boolean(string='Correo Parte de Horas')

