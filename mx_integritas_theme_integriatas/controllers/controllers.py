# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import requests
import logging
import xml.etree.ElementTree as ET
import asyncio
from datetime import datetime

_logger = logging.getLogger(__name__)

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

		#eti=request.env['crm.tag'].sudo().search([('name', '=','Boton whatsapp')])
		source_id = request.env['utm.source'].sudo().search([('name', '=','Boton whatsapp')])
		medium_id = request.env['utm.medium'].sudo().search([('name', '=','Website')])
		if not source_id:
			source_id=request.env['utm.source'].sudo().create({'name':'Boton Whatsapp'})
		if not medium_id:
			medium_id = request.env['utm.medium'].sudo().create({'name':'Website'})
		oportunidad = request.env['crm.lead'].sudo().create({'name':'Oportunidad WhatsApp Sitio Web '+name,'partner_id':bp.id,'source_id':source_id.id, 'medium_id' : medium_id.id })

		return str(oportunidad)
	@http.route(['/whatsapp/get_text'], type='json', auth='public', methods=['POST'], website=True, csrf=False)
	def getText(self, **post):
		website_id = request.website.id

		texto = "Hola, ¿Te gustaría solicitar información o una cotización? Ingresa tu email y número telefónico para ponernos en contacto contigo."
		query = request.env['website'].sudo().search([('id', '=',website_id)])
		if query.text_whatsapp:
			texto = query.text_whatsapp
		return texto
	@http.route(['/whatsapp/request'], type='json', auth='public', methods=['POST'], website=True, csrf=False)
	def getDataAPI(self, **post):
		_logger.warning(post.get("channel"))
		_logger.warning("==========")
		_logger.warning(request)
		return 'success', 200