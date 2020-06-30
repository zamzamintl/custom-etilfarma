# Copyright 2015 Camptocamp SA
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    marks = fields.Char(string="Marks") 

    @api.onchange("order_type")
    def onchange_order_type_marks(self):
        for record in self:
            if record.order_type_foreign:
                if record.env.user.marks:
                    record.marks = record.env.user.marks

    @api.onchange("invoice_to")
    def onchange_order_type_invoice_to(self):
        for record in self:
            if record.invoice_to.marks:
                record.marks = record.invoice_to.marks
            else:
                record.marks = ""