# Copyright 2020 Partner Guest House
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import _, api, fields, models, tools


class HrPayslip(models.Model):
    _name = "hr.payslip"
    _inherit = ["hr.payslip", "tier.validation"]
    _state_from = ["draft"]
    _state_to = ["done"]

    @api.model
    def _get_under_validation_exceptions(self):
        res = super(HrPayslip, self)._get_under_validation_exceptions()
        res.append("line_ids")
        res.append("number")
        return res
