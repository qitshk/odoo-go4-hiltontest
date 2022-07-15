# -*- coding: utf-8 -*-
{
    'name': "go4_view_change",

    'summary': """
        View customization for Go4Fiber""",

    'description': """
        1. Sales Quotation: disable 'Create & Edit' features under:\n
        - Customer field\n
        - Product field in sale order line\n
        2. Product Forecast Report: Hidden stock value field\n
        3. Sales Quotation printed PDF Repeat table header\n
    """,

    'author': "Hilton Wong",
    'website': "https://www.quick-it-support.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '14.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale_management', 'stock_account'],

    # always loaded
    'data': [
        'views/view_order_form_inherit.xml',
        'views/stock_account_report_product_product_replenishment_inherit.xml',
        'views/report_saleorder_doc_142da6d6-2b30-4c64-bc43-d364b24641d6_inherit.xml',
    ],
}
