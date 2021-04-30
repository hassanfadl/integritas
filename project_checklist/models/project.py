# -*- coding: utf-8 -*-

from odoo import fields, models, api, _
from odoo.exceptions import UserError, ValidationError

class ProjectChecklist(models.Model):
    _name = 'project.checklist'
    _description = 'Project Checklist'

    name = fields.Char(required="True")
    description = fields.Text()


class Project(models.Model):
    _inherit = 'project.project'

    project_checklist = fields.Many2many('project.checklist', 'project_checklist_rel', 'checklist_id', 'project_id', 'Project Checklist', default=0.0)
    check_marked = fields.Float('Checklist status', compute='_compute_check_marked',store=True)
    max_exit_value = fields.Float(compute='_get_max_exit_count', default=0.0)
    max_value = fields.Float(default=100.0)

    def _get_max_exit_count(self):
        for rec in self:
            all_checklist = self.env['project.checklist'].search([])
            rec.max_exit_value = len(all_checklist)

    @api.depends('project_checklist')
    def _compute_check_marked(self):
        all_checklist = self.env['project.checklist'].search([])
        if len(all_checklist) >=1 : 
            for rec in self:
                selected_checklist = rec.project_checklist
                rec.check_marked = (len(selected_checklist)* 100)/len(all_checklist)

