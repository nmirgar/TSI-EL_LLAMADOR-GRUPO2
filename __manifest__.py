# -*- coding: utf-8 -*-
{    'name': "llamador",

    'summary': """Gestión de la Semana Santa""",

    'description': """
        Módulo que nos proporciona la gestión de varios ámbitos de la Semana Santa
    """,

    'author': "Grupo 2",
    'website': "https://www.grupo2.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'reports/reports.xml',
        'reports/hermano_reports.xml',
        'reports/hermandad_report.xml',
        'views/hermandad_view.xml',
        'views/almacen_view.xml',
        'views/enseres_view.xml',
        'views/paso_view.xml',
        'views/donacion_view.xml',
        'views/hermano_view.xml',
        'views/puntorecorrido_view.xml',
        'views/rol_view.xml',
        'views/papeleta_view.xml',
        'views/tramo_view.xml',
        'views/evento_view.xml',
        'views/tipoevento_view.xml',
        'views/menus.xml',        
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/llamador.hermano.csv',
    ],
}