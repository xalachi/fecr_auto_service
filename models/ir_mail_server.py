# -*- coding: utf-8 -*-
from odoo import _, api, fields, models


class IrMailServer(models.Model):
    _inherit = 'ir.mail_server'

    smtp_user = fields.Char(groups=None)
    smtp_pass = fields.Char(groups=None)
