.. image:: https://img.shields.io/badge/license-AGPL--3-blue.png
   :target: https://www.gnu.org/licenses/agpl
   :alt: License: AGPL-3

========================
Payroll Tier Validation
========================

This module extends the functionality of Payroll Payslip to support a tier
validation process.

Installation
============

This module depends on ``base_tier_validation``. You can find it at
`OCA/server-ux <https://github.com/OCA/server-ux>`_

Configuration
=============

To configure this module, you need to:

#. Go to *Settings > Technical > Tier Validations > Tier Definition*.
#. Create as many tiers as you want for Payslip model.

Usage
=====

To use this module, you need to:

#. Create a Payslip triggering at least one "Tier Definition".
#. Click on *Request Validation* button.
#. Under the tab *Reviews* have a look to pending reviews and their statuses.
#. Once all reviews are validated click on *Confirm*.

Additional features:

* You can filter the Payslips requesting your review through the filter *Needs my
  Review*.
* User with rights to confirm the Payslip (validate all tiers that would
  be generated) can directly do the operation, this is, there is no need for
  her/him to request a validation.

Contributors
------------

* Volodymyr Bezliudnyi <vb@partnerguesthouse.com>

