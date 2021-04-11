# -*- coding: utf-8 -*-
from odoo import _, api, fields, models


class AccointInvoiceMail(models.Model):
    _name = 'account.invoice.mail'
    _description = 'Email to use in CC Invoices'

    name = fields.Char(
        string='Email',
        index=True,
    )
