from odoo import fields, models, api
import math


class AccountMoveInherit(models.Model):
    _inherit = 'account.move'

    # extra_id = fields.Many2one('account.move.line' ,string="Extra Discount") 
    special_disc_or_amt=fields.Selection([('none','No Discount'),('perc','Perc'),('amt','Amount')],string="Disc Perc/Amt", default = 'none')

    
    
    
    patient_groupp = fields.Char(string="Patient Group", compute="_compute_patient_group", store=True)

    @api.depends('partner_id.group_id')
    def _compute_patient_group(self):
        for record in self:
            record.patient_groupp = record.partner_id.group_id.name if record.partner_id.group_id else ''
   




    @api.depends('special_disc','line_ids.matched_debit_ids.debit_move_id.move_id.payment_id.is_matched',
        'line_ids.matched_debit_ids.debit_move_id.move_id.line_ids.amount_residual',
        'line_ids.matched_debit_ids.debit_move_id.move_id.line_ids.amount_residual_currency',
        'line_ids.matched_credit_ids.credit_move_id.move_id.payment_id.is_matched',
        'line_ids.matched_credit_ids.credit_move_id.move_id.line_ids.amount_residual',
        'line_ids.matched_credit_ids.credit_move_id.move_id.line_ids.amount_residual_currency',
        'line_ids.balance',
        'line_ids.currency_id',
        'line_ids.amount_currency',
        'line_ids.amount_residual',
        'line_ids.amount_residual_currency',
        'line_ids.payment_id.state',
        'line_ids.full_reconcile_id','amount_total','total_cost','special_disc_or_amt',
        'discount_amt',
        'state')
    def _compute_amount(self):
        res = super(AccountMoveInherit, self)._compute_amount()

        
        for rec in self:

            amount_untaxed_total_new = 0.0
            sub_total = 0.0
            amount_untaxed_total = 0.0
            
            rec.special_disc_amt = (sub_total*rec.special_disc)/100
            
            amount_untaxed_total = sum(line.price_unit for line in rec.invoice_line_ids)
            sub_total = sum(line.price_subtotal for line in rec.invoice_line_ids)
            amount_untaxed_total_new = amount_untaxed_total
                

            rec.amount_untaxed = amount_untaxed_total_new
            amt_total = sub_total
            

            # rec.amount_untaxed
            
            if rec.special_disc_or_amt == 'perc':
            
                            
                if rec.special_disc > 0 :
                    # total_lines = len(rec.invoice_line_ids)
                    # rec.invoice_line_ids.discount = rec.discount_amt + (rec.special_disc/total_lines)
                    

                    
                    # disc_price = (rec.special_disc*sub_total)/100 
                    # print("YE lleeeeeeeeeeee disc_price---0--",disc_price)
                    # disc_amt1 = sub_total - disc_price
                    # print("YE lleeeeeeeeeeee disc_amt1---0--",disc_amt1)

                    # disc_amt2 = amount_untaxed_total - disc_amt1
                    # print("YE lleeeeeeeeeeee disc_amt2---0--",disc_amt2)

                    # disc_perc = (disc_amt2/amount_untaxed_total)*100
                    # print("YE lleeeeeeeeeeee disc_amt2---0--",disc_perc)
                    
                    # disc_percent = disc_perc - rec.special_disc
                    total_lines = len(rec.invoice_line_ids)
                    rec.invoice_line_ids.discount = rec.discount_amt + (rec.special_disc/total_lines)
                    rec.total_cost = amt_total
                    
                    

                            
                        # line.discount = rec.discount_amt + (disc_perc/total_lines)
                        # line.discount = rec.discount_amt + ((((((line.price_unit - avg_disc )*rec.special_disc)/100)/(line.price_unit - avg_disc ))*100)/total_lines)
                        
                else:
                    
                    rec.invoice_line_ids.discount = rec.discount_amt
                    rec.total_cost = amt_total

            
                    # rec.discount_amt += rec.special_disc
                # else:
                    # for line in rec.invoice_line_ids:
                    #     line.discount = rec.discount_amt
                amt_total = rec.amount_untaxed - rec.discount_total
                
            elif rec.special_disc_or_amt == 'amt':
                
                if rec.special_disc > 0 :
                    for line in rec.invoice_line_ids:
                        total_lines = len(rec.invoice_line_ids)
                        proportional_discount = (rec.special_disc / total_lines) / line.price_unit * 100
                        line.discount = rec.discount_amt + proportional_discount
                    rec.total_cost = amt_total

                else:
                    for line in rec.invoice_line_ids:
                        line.discount = rec.discount_amt
                        rec.total_cost = amt_total

                amt_total = rec.amount_untaxed - rec.discount_total
            
            elif rec.special_disc_or_amt == '': 
                for line in rec.invoice_line_ids:
                    line.discount = rec.discount_amt
                amt_total = rec.amount_untaxed - rec.discount_total
                rec.total_cost = amt_total


            else:
                for line in rec.invoice_line_ids:
                    line.discount = rec.discount_amt
                amt_total = rec.amount_untaxed - rec.discount_total
                rec.total_cost = amt_total

            
                # for line in rec.invoice_line_ids:
                    # line.price_subtotal = line.price_unit - ((line.price_unit * rec.discount_amt)/100)

            rec.amount_total = amt_total
            rec.total_cost = amt_total
                
                # if rec.special_disc_or_amt == 'perc':

                # elif rec.special_disc_or_amt == 'amt':
                #     rec.total_cost = sub_total - rec.special_disc

                # else:
                #     rec.total_cost = rec.amount_untaxed - rec.discount_total
                
                
                
        # rec.invoice_line_ids.write({'discount': discount_factor})



