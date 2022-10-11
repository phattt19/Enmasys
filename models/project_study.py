from odoo import fields, models


class ProjectStudy(models.Model):
    _name = "project.study"
    _description = 'Project'

    name = fields.Char(string="Name", required=True)
    deadline = fields.Date(string='DeadLine', required=True)
    assigned_to_id = fields.Many2one('res.users', string='Assigned To')
    note = fields.Text(string='Note')
    description = fields.Html(string='Description')
    status = fields.Selection([('todo', 'TODO'),
                               ('pro', 'IN-PROGRESS'),
                               ('rv', 'REVIEW'),
                               ('done', 'DONE')],
                              string='Status', default='todo')

    managers_ids = fields.Many2many('res.users',
                                    'manager_project_user_rel',
                                    'manager_project_id',
                                    'user_id',
                                    string="Project Managers")

    attendee_ids = fields.One2many('res.users', 'x_user_id', string='Task Attendees')


class User(models.Model):
    _inherit = 'res.users'

    x_user_id = fields.Many2one('project.study')

