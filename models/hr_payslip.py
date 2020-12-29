# Copyright 2020 Partner Guest House
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models


class HrPayslip(models.Model):
    _name = "hr.payslip"
    _inherit = ["hr.payslip", "tier.validation"]
    _state_from = ["draft"]
    _state_to = ["done"]
