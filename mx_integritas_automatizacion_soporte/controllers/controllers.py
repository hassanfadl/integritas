# -*- coding: utf-8 -*-
from odoo import http

# class MxIntegritasAutomatizacionSoporte(http.Controller):
#     @http.route('/mx_integritas_automatizacion_soporte/mx_integritas_automatizacion_soporte/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mx_integritas_automatizacion_soporte/mx_integritas_automatizacion_soporte/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('mx_integritas_automatizacion_soporte.listing', {
#             'root': '/mx_integritas_automatizacion_soporte/mx_integritas_automatizacion_soporte',
#             'objects': http.request.env['mx_integritas_automatizacion_soporte.mx_integritas_automatizacion_soporte'].search([]),
#         })

#     @http.route('/mx_integritas_automatizacion_soporte/mx_integritas_automatizacion_soporte/objects/<model("mx_integritas_automatizacion_soporte.mx_integritas_automatizacion_soporte"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mx_integritas_automatizacion_soporte.object', {
#             'object': obj
#         })