# -*- coding: utf-8 -*-
{
    'name': "mx_integritas_timesheet/",
    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Envia el reporte de horas a los clientes cada mes.
    """,

    'author': "Integritas",
    'website': "http://integritas.mx",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base','sale_timesheet', 'timesheet_grid','project'],
    'data': [
        'views/views.xml',
        'views/templates.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
}
