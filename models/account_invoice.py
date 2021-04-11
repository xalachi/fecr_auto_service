# -*- coding: utf-8 -*-
from odoo import _, api, fields, models
from odoo.exceptions import UserError


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    email_cc_ids = fields.Many2many(
        comodel_name='account.invoice.mail',
    )
    email_cc_string = fields.Char(
        compute='_get_email_cc_string',
        store=True,
    )
    tipo_documento = fields.Selection(
        default='FE',
    )

    @api.depends('email_cc_ids')
    def _get_email_cc_string(self):
        for invoice in self:
            invoice.email_cc_string = ','.join(invoice.email_cc_ids.mapped('name'))

    def restrict_invoices(function):
        def wrapper(*args, **kwargs):
            self = args[0]
            company = self.env['res.company']._company_default_get('account.invoice')
            if company.invoices_available <= 0:
                raise UserError('You do not have more Invoices Available, please contact support')
            if len(self) > company.invoices_available:
                raise UserError('You do not have enough Invoices Available, please contact support')
            if company.expiration_date and company.expiration_date < fields.Date.context_today(self):
                raise UserError('Your subscription is no more valid, please contact support')
            function(*args, **kwargs)
            company.invoices_available -= len(self)

        return wrapper

    @restrict_invoices
    def action_invoice_open(self):
        return super(AccountInvoice, self).action_invoice_open()

    @api.onchange('partner_id', 'company_id')
    def _onchange_partner_id(self):
        super(AccountInvoice, self)._onchange_partner_id()
        self.tipo_documento = 'FE'
