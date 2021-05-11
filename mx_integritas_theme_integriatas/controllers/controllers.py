# -*- coding: utf-8 -*-
# from odoo import http


# class MxIntegritasThemeIntegriatas/(http.Controller):
#     @http.route('/mx_integritas_theme_integriatas//mx_integritas_theme_integriatas//', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mx_integritas_theme_integriatas//mx_integritas_theme_integriatas//objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('mx_integritas_theme_integriatas/.listing', {
#             'root': '/mx_integritas_theme_integriatas//mx_integritas_theme_integriatas/',
#             'objects': http.request.env['mx_integritas_theme_integriatas/.mx_integritas_theme_integriatas/'].search([]),
#         })

#     @http.route('/mx_integritas_theme_integriatas//mx_integritas_theme_integriatas//objects/<model("mx_integritas_theme_integriatas/.mx_integritas_theme_integriatas/"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mx_integritas_theme_integriatas/.object', {
#             'object': obj
#         })
