# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import requests
import xml.etree.ElementTree as ET
from datetime import datetime



class MxIntegritasThemeIntegriatas(http.Controller):
	@http.route(['/whatsapp/crear_oportunidad'], type='json', auth='public', methods=['POST'], website=True, csrf=False)
	def create_oportunity(self, **post):
		print("hola Cotizacion")
		name = post.get('name')
		email = post.get('email')
		phone = post.get('phone')
        
        
        
        
        
		bp=request.env['res.partner'].sudo().search([('email', '=', email)])

		if len(bp)>1:
			bp=request.env['res.partner'].sudo().search([('email', '=', email)])[0]
        
		if not bp:
			bp=request.env['res.partner'].sudo().create({'name': name,'email':email,'phone':phone})

		eti=request.env['crm.tag'].sudo().search([('name', '=','Boton whatsapp')])
		if not eti:
			eti=request.env['crm.tag'].sudo().create({'name':'Boton whatsapp'})
		tags=request.env['crm.tag'].sudo().browse(eti.id)
		oportunidad=request.env['crm.lead'].sudo().create({'name':'Oportunidad WhatsApp Sitio Web '+name,'partner_id':bp.id,'tag_ids':tags })

		return str(oportunidad)
