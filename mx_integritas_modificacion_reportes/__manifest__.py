# -*- coding: utf-8 -*-
{
    'name': "mx_integritas_modificacion_reportes/",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Modificación de reportes.
    """,

    'author': "Integritas",
    'website': "http://www.integritas.mx",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base', 'sale'],
    'data': [
        'views/sale_order.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
}
