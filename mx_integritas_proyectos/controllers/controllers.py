# -*- coding: utf-8 -*-
from odoo import http

# class MxIntegritasProyectos(http.Controller):
#     @http.route('/mx_integritas_proyectos/mx_integritas_proyectos/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mx_integritas_proyectos/mx_integritas_proyectos/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('mx_integritas_proyectos.listing', {
#             'root': '/mx_integritas_proyectos/mx_integritas_proyectos',
#             'objects': http.request.env['mx_integritas_proyectos.mx_integritas_proyectos'].search([]),
#         })

#     @http.route('/mx_integritas_proyectos/mx_integritas_proyectos/objects/<model("mx_integritas_proyectos.mx_integritas_proyectos"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mx_integritas_proyectos.object', {
#             'object': obj
#         })