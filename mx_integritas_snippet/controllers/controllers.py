# -*- coding: utf-8 -*-
# from odoo import http


# class /odoo/custom/addons/mxIntegritasSnippet(http.Controller):
#     @http.route('//odoo/custom/addons/mx_integritas_snippet//odoo/custom/addons/mx_integritas_snippet/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('//odoo/custom/addons/mx_integritas_snippet//odoo/custom/addons/mx_integritas_snippet/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('/odoo/custom/addons/mx_integritas_snippet.listing', {
#             'root': '//odoo/custom/addons/mx_integritas_snippet//odoo/custom/addons/mx_integritas_snippet',
#             'objects': http.request.env['/odoo/custom/addons/mx_integritas_snippet./odoo/custom/addons/mx_integritas_snippet'].search([]),
#         })

#     @http.route('//odoo/custom/addons/mx_integritas_snippet//odoo/custom/addons/mx_integritas_snippet/objects/<model("/odoo/custom/addons/mx_integritas_snippet./odoo/custom/addons/mx_integritas_snippet"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('/odoo/custom/addons/mx_integritas_snippet.object', {
#             'object': obj
#         })
