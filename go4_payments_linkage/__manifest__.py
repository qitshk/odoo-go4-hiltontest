# -*- coding: utf-8 -*-
{
    'name': "go4_payments_linkage",

    'summary': """
        Create view to map Accounting/Invoices to its related payments""",

    'description': """
        1. Create a Computed One2Many field and View from Accounting/Invoices (Model: Journal Entry) to Accounting/Payments (Model:Payments)
    """,

    'author': "Hilton Wong",
    'website': "https://www.quick-it-support.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '14.0.2',

    # any module necessary for this one to work correctly
    'depends': ['base', 'account'],

    # always loaded
    'data': [
        'views/view_move_form_inherit.xml',
    ],

}
