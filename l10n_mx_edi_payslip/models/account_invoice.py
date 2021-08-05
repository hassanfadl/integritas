# coding: utf-8
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import fields, models, _
from pytz import timezone

class HrContract(models.Model):
    _inherit = 'account.move'


    def _l10n_mx_edi_get_timezone(self, state):
        # northwest area
        if state == 'BCN':
            return timezone('America/Tijuana')
        # Southeast area
        elif state == 'ROO':
            return timezone('America/Cancun')
        # Pacific area
        elif state in ('BCS', 'CHH', 'SIN', 'NAY'):
            return timezone('America/Chihuahua')
        # Sonora
        elif state == 'SON':
            return timezone('America/Hermosillo')
        # By default, takes the central area timezone
        return timezone('America/Mexico_City')