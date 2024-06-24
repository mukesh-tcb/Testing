from odoo import models, fields, api

class XraySizeMaster(models.Model):
    _name = 'xray.size.master'
    _description = 'X-ray Size master'

    name = fields.Char(string="Size")
    details = fields.Char(string="Details")
    # item_category_ids = fields.Many2many('item.category', string='Item Categories')

class XraySizeInherit(models.Model):
    _inherit = 'product.template'

    xray_size = fields.Many2one('xray.size.master',string="X-ray Size")


