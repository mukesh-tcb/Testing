from odoo import models, fields, api

class MedicalLabNameInherit(models.Model):
    _inherit = 'medical.lab.list'

    tests_name = fields.Many2many('product.template', string="Test Names")
    # test_cost = fields.Many2one('product.template', string="Test Cost")
    lab_test_cost = fields.Float(string="Test Cost" , related = 'product_id.standard_price')

    # @api.depends('tests_name')
    # def _compute_test_cost(self):
    #     for record in self:
    #         if record.tests_name:
    #             record.test_cost = record.tests_name[0]  # Assuming you want to take the first test's cost
    #         else:
    #             record.test_cost = False

    # @api.onchange('product_id')
    # def _compute_test_cost(self):
    #     if self.product_id:
    #         check = self.env['product.template'].search([('name','=',self.product_id)])
    #         if check:
    #             self.lab_test_cost = check.standard_price