from odoo import fields, models


class ProjectStudy(models.Model):
    _name = "task2.enmasys"
    _description = 'Project'

    name = fields.Char(string="Name", required=True)
    deadline = fields.Date(string='DeadLine', required=True)
    assigned_to_id = fields.Many2one('study.enmasys', string='Assigned To')
    note = fields.Text(string='Note')
    description = fields.Html(string='Description')
    status = fields.Selection([('todo', 'TODO'),
                               ('pro', 'IN-PROGRESS'),
                               ('rv', 'REVIEW'),
                               ('done', 'DONE')],
                              string='Status', default='todo')

    managers_ids = fields.Many2many('study.enmasys',
                                    'managerproject_user_rel',
                                    'manager_project_id',
                                    'user_id',
                                    string="Project Managers")

    attendee_ids = fields.One2many('study.enmasys',
                                   inverse_name='user',
                                   string='Task Attendees')
