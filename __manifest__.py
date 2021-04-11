# -*- coding: utf-8 -*-
{
    'name': 'FECR Auto-Service',
    'version': '12.0.1.7.0',
    'author': 'HomebrewSoft',
    'website': 'https://gitlab.com/HomebrewSoft/fecr/fecr_auto_service',
    'depends': [
        'fecr',
        'stock',
        'web',
    ],
    'data': [
        # security
        'security/groups.xml',
        'security/rules.xml',
        'security/ir.model.access.csv',
        # data
        'data/act_url.xml',
        # reports
        'reports/account_invoice.xml',
        # views
        'views/account_invoice.xml',
        'views/ir_mail_server.xml',
        'views/res_company.xml',
        'views/menu.xml',
        'views/res_users.xml',
    ],
    'qweb': [
        'static/src/xml/menu.xml',
    ],
}
