from odoo import models, fields, api

class LabCalcInherit(models.Model):
    _inherit = 'lab.calc'



    normal_start = fields.Char('Normal Start Range')
    normal_end = fields.Char('Normal End Range')



class EnterResultInherit(models.Model):
    _inherit = 'enter.result'


    range_from = fields.Char(string='Range From')
    range_to = fields.Char(string='Range To')
    result = fields.Char(string='Result')
    @api.onchange('result')
    def onchange_result(self):      
        for rec in self:

            if rec.result:
                try:
                    result_value = float(rec.result)
                    range_from_value = float(rec.range_from) if rec.range_from else None
                    range_to_value = float(rec.range_to) if rec.range_to else None

                    if range_from_value is not None and result_value < range_from_value:
                        rec.res = 'low'
                    elif range_to_value is not None and result_value > range_to_value:
                        rec.res = 'high'
                    else:
                        rec.res = 'normal'
                except ValueError:
                    
                    rec.res = ''
            else:
                rec.res = ''

                    
                    
               