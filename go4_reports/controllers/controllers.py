# -*- coding: utf-8 -*-
# from odoo import http


# class Go4Cust(http.Controller):
#     @http.route('/go4_cust/go4_cust/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/go4_cust/go4_cust/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('go4_cust.listing', {
#             'root': '/go4_cust/go4_cust',
#             'objects': http.request.env['go4_cust.go4_cust'].search([]),
#         })

#     @http.route('/go4_cust/go4_cust/objects/<model("go4_cust.go4_cust"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('go4_cust.object', {
#             'object': obj
#         })
