# -*- coding: utf-8 -*-
{
    "name": "go4_reports",
    "summary": """
        PDF report customization for Go4Fiber""",
    "description": """
        1. Add SO/INV/DO no. in footer for:\n
        - Quotation/SO PDF report\n
        - Invoice with Payment PDF report\n
        - Invoice without Payment PDF report\n
        - Delivery Note - ALL PDF report\n
        - Delivery Note - In Stock PDF report\n\n

        2. Quotation/SO PDF report: Quotation No. add Revision\n
        3. Printed Header Format: Widen company address column

    """,
    "author": "Hilton Wong",
    "website": "https://www.quick-it-support.com",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    "category": "Uncategorized",
    "version": "14.0.1",
    # any module necessary for this one to work correctly
    "depends": ["base", "sale_management"],
    # always loaded
    "data": [
        "views/report_saleorder_document_copy_1_inherit.xml",  # quotation/SO
        "views/report_invoice_document_go4fiber_jsi_copy_1_inherit.xml",  # Invoice with payment
        "views/report_invoice_document_go4fiber_jsi_copy_2_inherit.xml",  # Invoice without payment
        "views/report_delivery_document_copy_5_copy_2_inherit.xml",  # delivery order - ALL
        "views/report_delivery_document_copy_5_inherit.xml",  # delivery order - In Stock
        "views/external_layout_boxed_inherit.xml",
    ],
    # only loaded in demonstration mode
    # "demo": ["demo/demo.xml",],
}
