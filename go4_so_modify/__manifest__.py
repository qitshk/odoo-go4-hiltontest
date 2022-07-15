# -*- coding: utf-8 -*-
{
    'name': "go4_so_modify",

    'summary': """
        Able to delete a Sales Order Line even the Sales Order is in confirmed status
    """,

    'description': """
        1. Allow SO in confirmed status to be able to delete.
        2. Raise UserError if user trying to delete the last Sales Order Line to prevent Invoice Count Wizid detech problem
        3. Raise UserError if user trying to delete a downpayment line which has already issued an invoice
    """,

    'author': "Hilton Wong",
    'website': "https://www.quick-it-support.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '14.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale_management'],

}
