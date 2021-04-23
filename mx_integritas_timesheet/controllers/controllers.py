# -*- coding: utf-8 -*-
# from odoo import http


# class MxIntegritasTimesheet/(http.Controller):
#     @http.route('/mx_integritas_timesheet//mx_integritas_timesheet//', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mx_integritas_timesheet//mx_integritas_timesheet//objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('mx_integritas_timesheet/.listing', {
#             'root': '/mx_integritas_timesheet//mx_integritas_timesheet/',
#             'objects': http.request.env['mx_integritas_timesheet/.mx_integritas_timesheet/'].search([]),
#         })

#     @http.route('/mx_integritas_timesheet//mx_integritas_timesheet//objects/<model("mx_integritas_timesheet/.mx_integritas_timesheet/"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mx_integritas_timesheet/.object', {
#             'object': obj
#         })
