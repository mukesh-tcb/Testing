
from odoo import models, fields, api
from odoo.exceptions import UserError
from odoo.fields import Command
from odoo.tools import float_is_zero
from datetime import datetime,time 

class SaleAdvancePaymentInv(models.TransientModel):
    _inherit = 'sale.advance.payment.inv'


    

    # @api.model
    # def create(self, vals):
    #     record = super(SaleAdvancePaymentInv, self).create(vals)
    #     record.create_invoices()
    #     return record


    # def create_invoices(self):
    #     self._create_invoices(self.sale_order_ids)
    #     if self.env.context.get('open_invoices'):
    #         return self.sale_order_ids.action_view_invoice()
    #     return {'type': 'ir.actions.act_window_close'}
        # def create_invoices(self):
    #     self._create_invoices(self.sale_order_ids)
    #     order = self.sale_order_ids

    #     if self.env.context.get('open_invoices'):
    #         return self.sale_order_ids.action_view_invoice()

    #     down_payment_so_line = self.env['sale.order.line'].create(
    #             self._prepare_so_line_values(order)
    #         )

        

    #     invoice = self.env['account.move'].sudo().create(
    #             self._prepare_invoice_values(order, down_payment_so_line)
    #         ).with_user(self.env.uid)

    #     invoice.message_post_with_view(
    #             'mail.message_origin_link',
    #             values={'self': invoice, 'origin': order},
    #             subtype_id=self.env.ref('mail.mt_note').id)

    #     return {'type': 'ir.actions.act_window_close'}



class SaleOrder(models.Model):
    _inherit = 'sale.order'

    patient_id=fields.Many2one('res.partner',string="Patient Name")
    doctor_id = fields.Many2one('hr.employee','Doctor',required=True,domain="[('designation','=','Doctor')]")

    def action_create_direct_invoice(self):
        self.ensure_one()
      
        invoice = self.with_context(raise_if_nothing_to_invoice=False)._create_invoices()
        # product_templates = self.env['product.template'].search([])
        # product_templates.write({'check_bool': False})
        action = self.env.ref('account.action_move_out_invoice_type').read()[0]
        if invoice:
            action['views'] = [(self.env.ref('account.view_move_form').id, 'form')]
            action['res_id'] = invoice.id
        return action





    @api.depends('partner_id','apt_id')
    def comp_disc_perc(self):
    	for rec in self:
            if rec.partner_id and rec.hospital_bool==True:
                patient_group=self.env['patient.group'].search([('name','=',rec.partner_id.group_id.name)])
                if rec.apt_id:
                    if rec.apt_id.old_new=='old':
                        rec.disc_per=patient_group.new_dis_per
                    if rec.apt_id.old_new=='new':
                        rec.disc_per=patient_group.new_dis_per
                else:
                    rec.disc_per=patient_group.new_dis_per

    # @api.model
    # def create(self, vals):
    #     record = super(SaleOrder, self).create(vals)
    #     record.self.env['sale.advance.payment.inv'].create_invoice()
    #     return record
    # item_type = self.env['item.type'].search([('name','=','Lab')])
   
    # def action_view_sale_advance_payment_inv(self):
    #     # Call the original method
    #     # res = super(SaleOrder, self).action_view_sale_advance_payment_inv()

    #     # After calling the original method, redirect to the account.move form view
    #     payment_inv_wizard = self.env['sale.advance.payment.inv'].create({
    #         'sale_order_ids': [(6, 0, self.ids)],
    #         'advance_payment_method': 'delivered',
    #         'deduct_down_payments': True,
    #     })
    #     payment_inv_wizard.create_invoices()
    #     account_move_view_id = self.env.ref('account.view_move_form').id
    #     return {
    #         'type': 'ir.actions.act_window',
    #         'res_model': 'account.move',
    #         'view_type': 'form',
    #         'view_mode': 'form',
    #         'views': [(account_move_view_id, 'form')],
    #         'target': 'current',
    #         'context' : {
	# 													 # 'default_apt_id':self.id,
	# 													  'default_partner_id':self.partner_id.id,
	# 													  'default_patient_group':self.patient_group,
	# 													  'default_patient_id':self.patient_id,
	# 													  'default_order_type_sel':'lab',
	# 													#   'default_item_type_ids':self.env['patient.hospital.dashboard'].item_type.ids,
	# 													  'default_apt_id':self.env['patient.hospital.dashboard'].latest_appt_id.id,
	# 													  'default_doctor_id':self.doctor_id.id,
	# 													  'default_with_appointment':self.with_appointment,
	# 							}
    #     }


    # user_id = fields.Many2one('res.users', 'Doctor')

     