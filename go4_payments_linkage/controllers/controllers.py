# -*- coding: utf-8 -*-
# from odoo import http


# class Go4PaymentsLinkage(http.Controller):
#     @http.route('/go4_payments_linkage/go4_payments_linkage/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/go4_payments_linkage/go4_payments_linkage/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('go4_payments_linkage.listing', {
#             'root': '/go4_payments_linkage/go4_payments_linkage',
#             'objects': http.request.env['go4_payments_linkage.go4_payments_linkage'].search([]),
#         })

#     @http.route('/go4_payments_linkage/go4_payments_linkage/objects/<model("go4_payments_linkage.go4_payments_linkage"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('go4_payments_linkage.object', {
#             'object': obj
#         })
