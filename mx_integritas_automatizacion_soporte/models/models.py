# -*- coding: utf-8 -*-

from odoo import models, fields, api
import datetime
import smtplib
from email.mime.text import MIMEText
from email.header import Header
class mx_integritas_automatizacion_soporte(models.Model):
    _name = 'project.task'
    _inherit = ['project.task']
    print("INicio------")
   
        
        
    
    fecha_limite_pruebas = fields.Char(compute="_value_pc", string="CAmpo extra",traslate=True)
    
    @api.multi
    def _value_pc(self):
        print(self.name)
        if self.date_last_stage_update != False:
            days = 16
            days_added = datetime.timedelta(days = days)
            future_date_and_time = self.date_last_stage_update + days_added
            date_time_format = future_date_and_time.strftime("%d/%m/%Y %H:%M:%S")
            self.fecha_limite_pruebas = date_time_format
        else:
            self.fecha_limite_pruebas = False

    @api.multi   
    def enviar_email(self):
        
        e = Correo()
        print(len(self.env['project.task'].search([('active', '=', True)])))
        lent = self.env['project.task'].search([('active', '=', True)])
        for rec in lent:
            #print(self.env['project.task'].browse(rec.id).name)
            #print(self.env['project.task'].browse(rec.id).fecha_limite_pruebas)
            #print(self.env['project.task'].browse(rec.id).date_last_stage_update)
            
            date_last_stage_update = self.env['project.task'].browse(rec.id).date_last_stage_update
            _from = rec.email_from
            namePartner = rec.partner_id.name
            task = rec.name
            if date_last_stage_update != False:
                days = 1
                days_added = datetime.timedelta(days = days)
                future_date_and_time = date_last_stage_update + days_added
                date_time_format = future_date_and_time.strftime("%Y-%m-%d")
                #data_time_format_date = datetime.datetime.strptime(date_time_format, "%Y-%m-%d %H:%M:%S")

                print(date_last_stage_update.strftime("%Y-%m-%d"))
                print(date_time_format)
                print(datetime.datetime.now().date())
                if str(date_time_format) == str(datetime.datetime.now().date()):
                    print("EQUALS")
                    if rec.stage_id.name == 'Pruebas':
                        e.email_send(_from, task, namePartner)
                        
                
            else:
                self.fecha_limite_pruebas = False

    '''def email_send( self, _from, task, namePartner):
        if _from != "" and namePartner != "" and task != "":
            try:
                sender = 'edgar.molina@integritas.mx'
                password = 'EdgarDevelopment94'
                
                smtpObj = smtplib.SMTP(host='smtp.gmail.com', port=587)
                fruits = ["apple", "banana", "cherry"]
                smtpObj.ehlo()
                smtpObj.starttls()
                smtpObj.ehlo()
                smtpObj.login(user=sender, password=password)


                for x in fruits:
                    receivers = _from
                    message = """ Estimado """+namePartner+""":\nNo hemos recibido ninguna respuesta de su parte sobre la tarea """+str(task)+""" y en caso de no recibir ningún comentario procederemos a cerrarlo el día de mañana.\n\nQuedamos atentos a sus comentarios.\nReciban un cordial saludo
                    """
                    part2 = MIMEText(message, "plain", "utf-8")
                    part2['Subject'] = Header("REQUERIMOS UNA ACCIÓN DE SU PARTE", 'utf-8')
                    part2['Cc'] = sender
                    smtpObj.sendmail(sender, receivers, part2.as_string())
                    print("Successfully sent email")            
            except:
                print("An exception occurred")
            finally:
                smtpObj.quit()'''
    

class Correo:
    smtpObj = None
    sender = ""
    password = ""
    def __init__(self):
        print("INicializzzz")
        self.sender = 'development@integritas.mx'
        self.password = 'Djttr-01'
        
        self.smtpObj = smtplib.SMTP(host='smtp.gmail.com', port=587)
        self.smtpObj.ehlo()
        self.smtpObj.starttls()
        self.smtpObj.ehlo()
        self.smtpObj.login(user=self.sender, password=self.password)
    def email_send(self,  _from, task, namePartner):
        if _from != "" and namePartner != "" and task != "":
            print("----")
            print(self.sender)
            receivers = _from
            message = """ Estimado """+namePartner+""":\nNo hemos recibido ninguna respuesta de su parte sobre la tarea """+str(task)+""" y en caso de no recibir ningún comentario procederemos a cerrarlo el día de mañana.\n\nQuedamos atentos a sus comentarios.\nReciban un cordial saludo
            """
            part2 = MIMEText(message, "plain", "utf-8")
            part2['Subject'] = Header("REQUERIMOS UNA ACCIÓN DE SU PARTE", 'utf-8')
            part2['Cc'] = self.sender
            self.smtpObj.sendmail(self.sender, receivers, part2.as_string())
            print("Successfully sent email")            
            
            
      
