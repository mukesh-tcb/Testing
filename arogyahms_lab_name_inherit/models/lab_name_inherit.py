from odoo import fields, models,api
from datetime import datetime 


class LabUnitInherit(models.Model):
    _inherit = 'product.template'

    lab_name_ids = fields.Many2many("medical.lab.dep", string="Lab Name")
#     check_bool = fields.Boolean(string = "" ,default = False)
#     # from odoo import models, fields, api

# # class ProductTemplateInherit(models.Model):
# #     _inherit = 'product.template'

#     add_products_bool = fields.Boolean(string="Add Products Bool")
#     add_lines_bool = fields.Boolean(string="Add Lines Bool")
#     # is_added_to_order = fields.Boolean(string="Added to Order", compute='_compute_is_added_to_order', store=True)

#     def addd_liness(self):
#         active_id = self.env[self._context['active_model']].browse(self._context['active_id'])
#         product = self.env['product.template'].search([('id', '=', self.id)])

#         order_line = self.env['sale.order.line'].search([
#             ('order_id', '=', active_id.id),
#             ('product_id', '=', product.product_variant_id.id)
#         ])
#         if order_line:
#             order_line.unlink()
        
#         if self._context.get('view_id') != self.env.ref('sale.view_order_form').id:
#             product.add_products_bool = False
#             product.add_lines_bool = True
#             product.check_bool = False

#     @api.model
#     def addd_lines(self, val):
#         active_id = self.env[self._context['active_model']].browse(self._context['active_id'])
#         product = self.env['product.template'].search([('id', '=', val)])
        
        
        
#         product.add_products_bool = True
#         product.add_lines_bool = False
#         product.check_bool = True
        
        
#         new_line = active_id.order_line.create({
#             'order_id': active_id.id,
#             'name': product.name,
#             'product_uom_qty': 1,
#             'product_id': product.product_variant_id.id,
#             'product_template_id': self.id,
#             'product_uom': product.uom_id.id,
#             'customer_lead': 0,
#             'price_unit': product.standard_price,
            
#         })
        
        # if self._context.get('view_id') != self.env.ref('sale.view_order_form').id:
        #     product.add_products_bool = False
        #     product.add_lines_bool = True
        #     product.check_bool = False
    
    
    # def add_liness(self):
    #     active_id = self.env[self._context['active_model']].browse(self._context['active_id'])
    #     for line in active_id.order_line:
    #         if line.product_template_id.id == self.id:
    #             line.unlink()
    #     self.add_products_bool = False
    #     self.add_lines_bool = True

    # @api.model
    # def _toggle_add_buttons(self, val):
    #     product = self.env['product.template'].browse(val)
    #     product.add_products_bool = not product.add_products_bool
    #     product.add_lines_bool = not product.add_lines_bool  
        
    
    # testt_price = fields.Float(string="Selling Price" , related = 'product_id.standard_price')

    # lab_name = fields.Char(string="Name", related="medical.lab.dep.name")
    # def fetch_lab_name(env):
    #     lab_dep = env['medical.lab.dep'].search([], limit=1)
    #     if lab_dep:
    #         return lab_dep.name
    #     else:
    #         return None



