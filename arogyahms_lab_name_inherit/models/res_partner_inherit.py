from odoo import api, fields, models, _



class MedicalLabInherit(models.Model):
    _inherit = "res.partner"

    medical_historyy_ids = fields.Many2one('med.his.master',string="Medical History")
    
    group_id=fields.Many2one('patient.group',string='Patient Group')


