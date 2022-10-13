from odoo import fields, models, api
from datetime import datetime

from odoo.exceptions import ValidationError


class User(models.Model):
    _inherit = 'res.users'

    x_user_id = fields.Many2one('project.study')


class ProjectStudy(models.Model):
    _name = "project.study"
    _description = 'Project'

    name = fields.Char(string="Name", required=True)
    deadline = fields.Date(string='DeadLine', required=True)
    assigned_to_id = fields.Many2one('res.users', string='Assigned To', default=lambda self: self.env.user)
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

    assignee_update = fields.Datetime(string='Assignee Update At', compute='_compute_assignee_update', store=True)

    tags = fields.Selection([('old', 'Old Feature'),
                             ('new', 'New Feature')],
                            string='Tags')

    customer_id = fields.Many2one('res.partner', string='Customer')

    @api.depends('assigned_to_id')
    def _compute_assignee_update(self):
        for record in self:
            record.assignee_update = datetime.today().now()

    @api.onchange('assigned_to_id')
    def _onchange_assigned_to_id(self):
        self.tags = 'new'

    @api.constrains('customer_id')
    def _check_customer_id_exist(self):
        for cus in self:
            if cus.customer_id.id:
                condition = self.env['project.study'].search([('customer_id', '=', cus.customer_id.id),
                                                              ('id', '!=', cus.id)])
                if condition:
                    raise ValidationError(
                        "This customer is existed at another task. Please choose "
                        "another customer.")
