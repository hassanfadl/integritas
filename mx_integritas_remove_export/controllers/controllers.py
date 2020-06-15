# -*- coding: utf-8 -*-
from odoo import http

# class MxIntegritasRemoveExport(http.Controller):
#     @http.route('/mx_integritas_remove_export/mx_integritas_remove_export/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mx_integritas_remove_export/mx_integritas_remove_export/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('mx_integritas_remove_export.listing', {
#             'root': '/mx_integritas_remove_export/mx_integritas_remove_export',
#             'objects': http.request.env['mx_integritas_remove_export.mx_integritas_remove_export'].search([]),
#         })

#     @http.route('/mx_integritas_remove_export/mx_integritas_remove_export/objects/<model("mx_integritas_remove_export.mx_integritas_remove_export"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mx_integritas_remove_export.object', {
#             'object': obj
#         })