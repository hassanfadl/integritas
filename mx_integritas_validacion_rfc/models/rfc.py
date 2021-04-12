# -*- coding: utf-8 -*-

from odoo import api, fields, models
import os
import os.path
import subprocess

class mx_integritas_rfc_lista_negra(models.Model):
    _name = "mx_integritas_validacion_rfc.rfc"
    #_inherit = ['mail.thread']
    _description = "RFC Lista Negra"

    name = fields.Char(string='RFC',required=True)
    is_cancelado=fields.Boolean(string='Cancelado',default=False)
    is_condonado=fields.Boolean(string='Condonado',default=False)
    is_retorno_inversiones=fields.Boolean(string='Retorno de Inversiones',default=False)
    is_exigible=fields.Boolean(string='Exigible',default=False)
    is_firmes=fields.Boolean(string='Firmes',default=False)
    is_no_localizado=fields.Boolean(string='No Localizado',default=False)
    is_sentencia=fields.Boolean(string='Sentencia',default=False)
    is_valido=fields.Boolean(string='Valido',default=False)
    is_permitido=fields.Boolean(string='Permitir aun en Lista Negra',default=False)

    is_desvirtuado=fields.Boolean(string='Desvirtuado',default=False)
    is_definitivo=fields.Boolean(string='Definitivo',default=False)
    is_presuntos=fields.Boolean(string='Presuntos',default=False)
    is_sentenciasfavorables=fields.Boolean(string='Sentencias Favorables',default=False)
    act=fields.Char(string='Checado',default=False)


    def mx_integritas_proceso_lista_negra_sat(self,path):
    	sent=path
    	ls_output=subprocess.Popen(["sh", sent])
    
    

