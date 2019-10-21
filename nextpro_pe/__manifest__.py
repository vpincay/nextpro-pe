# -*- coding: utf-8 -*-
{
    'name': "NEXT-PRO Localizacion Peru",

    'summary': "Localizacion peru",

    'description': "Localizacion peru",

    'author': "Victor Pincay V.",
    'website': "http://www.next-pro.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Accounting',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'account', 'account_accountant', 'purchase', 'fleet', 'crm', 'stock' ],

    # always loaded
    'data': [
        # vistas de formulario/ listas
        'views/res_company_view.xml',
        'views/res_partner_view.xml',
        'views/catalogo_06_views.xml', 

        # seguridad
        'security/ir.model.access.csv',   
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}