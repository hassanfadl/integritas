# -*- coding: utf-8 -*-
from odoo import http
from odoo import http
from odoo.http import request
import requests
import xml.etree.ElementTree as ET
from datetime import datetime
class ControllerMassMailing(http.Controller):
    @http.route(['/save/addEmail'], type='http', auth='none', website=True, methods=['POST'], csrf=False)
    def api_rest(self, **post):
        #_logger.warning("Input Integritas")
        print("Francias turrentin")
        

        return str("hola")

    @http.route('/website_mass_mailing/subscribe/replace', type='json', website=True, auth="public")
    def subscribe(self, list_id, email,  **post):
        if not request.env['ir.http']._verify_request_recaptcha_token('website_mass_mailing_subscribe'):
            return {
                'toast_type': 'danger',
                'toast_content': _("Suspicious activity detected by Google reCaptcha."),
            }
        ContactSubscription = request.env['mailing.contact.subscription'].sudo()
        Contacts = request.env['mailing.contact'].sudo()
        name, email = Contacts.get_name_email(email)
        name = post['name']
        print(name)
        subscription = ContactSubscription.search([('list_id', '=', int(list_id)), ('contact_id.email', '=', email)], limit=1)
        if not subscription:
            # inline add_to_list as we've already called half of it
            contact_id = Contacts.search([('email', '=', email)], limit=1)
            if not contact_id:
                contact_id = Contacts.create({'name': name, 'email': email})
            ContactSubscription.create({'contact_id': contact_id.id, 'list_id': int(list_id)})
        elif subscription.opt_out:
            subscription.opt_out = False
        # add email to session
        request.session['mass_mailing_email'] = email
        mass_mailing_list = request.env['mailing.list'].sudo().browse(list_id)
        return {
            'toast_type': 'success',
            'toast_content': mass_mailing_list.toast_content
        }

