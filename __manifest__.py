# -*- coding: utf-8 -*-
{
    'name': "llamador",

    'summary': """Gestión de la Semana Santa""",

    'description': """
        Módulo que nos proporciona la gestión de varios ámbitos de la Semana Santa
    """,

    'author': "Manuel Revuelta Reyes",
    'website': "https://www.sleepyrazor.github.io",

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
        #'views/views.xml',
        'views/hermanos_view.xml',
        'views/menus.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/llamador.pasos.csv',
    ],
}
