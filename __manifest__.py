# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Payroll Tier Validation",
    "summary": "Extends the functionality of Payroll Payslip to support a tier validation process.",
    "version": "13.0.1.0.0",
    "category": "Payroll",
    "website": "https://www.partnerguesthouse.com",
    "author": "Partner Guest House",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": ["payroll", "base_tier_validation"],
    "data": ["views/hr_payslip_view.xml"],
}
