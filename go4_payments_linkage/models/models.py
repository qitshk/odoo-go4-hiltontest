from odoo import models, fields, api


class AccountMove(models.Model):
    _inherit = "account.move"

    # Computed One2Many field containing "account.payment(id)"
    payment_list = fields.One2many(
        comodel_name="account.payment", string="Payment List", compute="_compute_account_payment_ids")

    @api.depends('invoice_payments_widget')
    def _compute_account_payment_ids(self):
        for inv in self:
            payment_unique_list = []
            reconciled_vals = inv._get_reconciled_info_JSON_values()
            # Extract from DICT key "account_payment_id" which is reconciled payment records for related invoice
            payment_id_list = [rec["account_payment_id"]
                                for rec in reconciled_vals]
            # Prevent duplicate "account_payment_id" record in "payment_list" O2M field that causes error
            for idx in payment_id_list:
                if idx not in payment_unique_list:
                    payment_unique_list.append(idx)
                inv.payment_list = payment_unique_list
            # Need to force return for null "payment_list" to prevent compute field assignment error
            return inv.payment_list
