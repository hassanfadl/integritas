# -*- coding: utf-8 -*-
# from odoo import http


# class MxIntegritasEbooks(http.Controller):
#     @http.route('/mx_integritas_ebooks/mx_integritas_ebooks/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mx_integritas_ebooks/mx_integritas_ebooks/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('mx_integritas_ebooks.listing', {
#             'root': '/mx_integritas_ebooks/mx_integritas_ebooks',
#             'objects': http.request.env['mx_integritas_ebooks.mx_integritas_ebooks'].search([]),
#         })

#     @http.route('/mx_integritas_ebooks/mx_integritas_ebooks/objects/<model("mx_integritas_ebooks.mx_integritas_ebooks"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mx_integritas_ebooks.object', {
#             'object': obj
#         })
