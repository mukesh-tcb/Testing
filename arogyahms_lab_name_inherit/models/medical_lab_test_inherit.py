from odoo import fields, models


class MedicalLabNameInherit(models.Model):
    _inherit = 'medical.lab.dep'

    tests_name = fields.Many2many('product.template', string="Test Name")
    
    # lab_name_ids = fields.Many2many("medical.lab.dep", string="Lab Name")
    
    

    
class PatientRemoveChildGenderInherit(models.Model):
    _inherit = 'res.partner'

    # gender_inherit= fields.Selection([
    #     ('male','Male'),
    #     ('female','Female'),
    #     ('other','Other')], string= "Gender *")
    # gender_id= fields.Selection([
    #     ('male','Male'),
    #     ('female','Female'),
    #     ('other','Other')], string= "Gender *")
    # def _filter_selection(self):
       
    #     gender_selection = dict(self.fields_get(allfields=['gender_inherit'])['gender_inherit']['selection'])
    #     return [(key, value) for key, value in gender_selection.items() if key != 'child']

    # gender_inherit = fields.Selection(selection=_filter_selection, string="Gender")
    

class AppointmentRemoveChildGenderInherit(models.Model):
    _inherit = 'medical.appointment'

    # gender_inherit= fields.Selection([
    #     ('male','Male'),
    #     ('female','Female'),
    #     ('other','Other')], string= "Gender")
    
    # gender_id= fields.Selection([
    #     ('male','Male'),
    #     ('female','Female'),
    #     ('other','Other')], string= "Gender")

    # def _filter_selection(self):
        
    #     gender_selection = dict(self.fields_get(allfields=['gender_inherit'])['gender_inherit']['selection'])
    #     return [(key, value) for key, value in gender_selection.items() if key != 'child']

    # gender_inherit = fields.Selection(selection=_filter_selection, string="Gender")



    
