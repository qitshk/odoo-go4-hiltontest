# -*- coding: utf-8 -*-

from odoo import models, _
from odoo.exceptions import UserError

class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    def _check_line_unlink(self):
        #Remove line.state = sale, so the sales.order.line can be deleted
        return self.filtered(lambda line: line.state == 'done' and (line.invoice_lines or not line.is_downpayment))

    def unlink(self):
        if self._check_line_unlink():
            raise UserError(_('You can not remove an order line once the sales order is locked.\nYou should rather set the quantity to 0.\nOr unlock this order for further process.\n\nBy Admin - Hilton'))
        if len(self.order_id.order_line) <= 1 and self.state in ('sale', 'done'):
            raise UserError(_('I do NOT suggest you to remove the last sales order line. You should cancel this order instead.\n\nBy Admin - Hilton'))
        #For multiple delete Sale Order Line to avoid singleton issue
        for line in self:
            if (line.is_downpayment and line.invoice_lines):
                raise UserError(_('The Deposit had already issued. I do NOT suggest you remove this line.\n\nBy Admin - Hilton'))
        return super(SaleOrderLine, self).unlink()