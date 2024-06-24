from odoo import models, fields, api

class LabCalcInherit(models.Model):
    _inherit = 'medical.appointment'
    
    
    
    @api.depends('opd_id','department_id','doctor_id','patient_group','old_new','waive_of')
    def compute_reg_feeee(self):
        for rec in self:
            if rec.opd_id:
                opd_id1 = self.env['opd.duty'].search([('opd_name','=',self.opd_id.name),('department_id','=',self.department_id.name),('staff','=',self.doctor_id.name)],limit=1)
                if rec.old_new=='old':
                    if rec.waive_of==True:
                        rec.reg_fee=0
                    else:
                        rec.reg_fee = opd_id1.old_reg_fee - (( opd_id1.old_reg_fee * rec.patient_group.new_dis_per)/100)
                else:
                    if rec.waive_of==True:
                        rec.reg_fee=0
                    else:
                        rec.reg_fee = opd_id1.new_reg_fee - (( opd_id1.new_reg_fee * rec.patient_group.new_dis_per)/100)
                        
                        
                        
                        
    @api.depends('doctor_id','patient_group','old_new','waive_of')
    def compute_consult_feeee(self):
            for rec in self:
                if rec.doctor_id:
                    if rec.old_new=='old':
                        if rec.waive_of==True:
                            rec.consult_fee=0
                        else:
                            rec.consult_fee = rec.doctor_id.consult_fee - (( rec.doctor_id.consult_fee * rec.patient_group.new_dis_per)/100)
                    else:
                        if rec.waive_of==True:
                            rec.consult_fee=0
                        else:
                            rec.consult_fee = rec.doctor_id.consult_fee_new - (( rec.doctor_id.consult_fee_new * rec.patient_group.new_dis_per)/100)
