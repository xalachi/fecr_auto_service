# -*- coding: utf-8 -*-
from odoo import _, api, fields, models


class ResCompany(models.Model):
    _inherit = 'res.company'

    invoices_available = fields.Integer(
        required=True,
        write=["fecr_auto_service.fecr_admin_group"],
    )
    expiration_date = fields.Date(
        required=True,
        track_visibility='onchange',
        write=["fecr_auto_service.fecr_admin_group"],
    )
