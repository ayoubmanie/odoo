# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'custom module (ayoub.2)',
    'version' : '1.0',
    'summary': 'custom',
    'sequence': 10,
    'description': """custom""",
    'category': 'Productivity',
    'website': 'https://www.odoo.com/app/invoicing',
    'images' : [],
    'depends' : [],
    'data': [],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'assets': {
        'web.assets_backend': [
            # 'customModule/static/src/css/flUhRq6tzZclQEJ-Vdg-IuiaDsNc.woff2',
            
            ("before","web/static/src/legacy/scss/primary_variables.scss",'customModule/static/src/css/colors.scss'),
            ("after","web/static/src/legacy/scss/utils.scss",'customModule/static/src/css/utils.scss'),
            'customModule/static/src/css/custom-odoo-css.scss',
        ],
    }
}