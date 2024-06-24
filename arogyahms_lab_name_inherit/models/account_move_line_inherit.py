from odoo import fields, models, api
import math


class AccountMoveInherit(models.Model):
    _inherit = 'account.move.line'
    
    extra_discount = fields.Float(string="Extra Discount")

    # @api.depends('move_id.special_disc', 'move_id.invoice_line_ids')
    # def _compute_extra_discount(self):
    #     for line in self:
    #         if line.move_id and line.move_id.invoice_line_ids:
    #             total_lines = len(line.move_id.invoice_line_ids)
    #             if total_lines > 0:
    #                 line.extra_discount = line.move_id.special_disc / total_lines
    #             else:
    #                 line.extra_discount = 0.0
    #         else:
    #             line.extra_discount = 0.0