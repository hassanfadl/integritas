# -*- coding: utf-8 -*-
# from odoo import http


# class MxIntegritasModificacionReportes/(http.Controller):
#     @http.route('/mx_integritas_modificacion_reportes//mx_integritas_modificacion_reportes//', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mx_integritas_modificacion_reportes//mx_integritas_modificacion_reportes//objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('mx_integritas_modificacion_reportes/.listing', {
#             'root': '/mx_integritas_modificacion_reportes//mx_integritas_modificacion_reportes/',
#             'objects': http.request.env['mx_integritas_modificacion_reportes/.mx_integritas_modificacion_reportes/'].search([]),
#         })

#     @http.route('/mx_integritas_modificacion_reportes//mx_integritas_modificacion_reportes//objects/<model("mx_integritas_modificacion_reportes/.mx_integritas_modificacion_reportes/"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mx_integritas_modificacion_reportes/.object', {
#             'object': obj
#         })
