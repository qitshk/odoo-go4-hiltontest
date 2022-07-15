# -*- coding: utf-8 -*-
# from odoo import http


# class Go4ViewChange(http.Controller):
#     @http.route('/go4_view_change/go4_view_change/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/go4_view_change/go4_view_change/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('go4_view_change.listing', {
#             'root': '/go4_view_change/go4_view_change',
#             'objects': http.request.env['go4_view_change.go4_view_change'].search([]),
#         })

#     @http.route('/go4_view_change/go4_view_change/objects/<model("go4_view_change.go4_view_change"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('go4_view_change.object', {
#             'object': obj
#         })
