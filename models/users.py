
from odoo import fields, models


class StudyEnmasys(models.Model):
    _name = "study.enmasys"
    _description = 'User'

    name = fields.Char(string="Name", required=True)
    image = fields.Binary(string='Image', attachment=True)
    country = fields.Char(string='Country')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender', default='male')
    day_of_birth = fields.Datetime(string='Day of birth')
    position = fields.Char('Position')
    height = fields.Float(string='Height')
    weight = fields.Float(string='Weight')
    color = fields.Integer('Color Index', default=0)
    user = fields.Many2one('task2.enmasys')

