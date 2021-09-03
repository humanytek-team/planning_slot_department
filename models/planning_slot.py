from odoo import api, fields, models


class PlanningSlot(models.Model):
    _inherit = "planning.slot"

    department_id = fields.Many2one(
        related="employee_id.department_id",
        store=True,
    )
