# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class go4_cust(models.Model):
#     _name = 'go4_cust.go4_cust'
#     _description = 'go4_cust.go4_cust'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
