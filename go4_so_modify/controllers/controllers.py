# -*- coding: utf-8 -*-
# from odoo import http


# class Go4SoModify(http.Controller):
#     @http.route('/go4_so_modify/go4_so_modify/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/go4_so_modify/go4_so_modify/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('go4_so_modify.listing', {
#             'root': '/go4_so_modify/go4_so_modify',
#             'objects': http.request.env['go4_so_modify.go4_so_modify'].search([]),
#         })

#     @http.route('/go4_so_modify/go4_so_modify/objects/<model("go4_so_modify.go4_so_modify"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('go4_so_modify.object', {
#             'object': obj
#         })
