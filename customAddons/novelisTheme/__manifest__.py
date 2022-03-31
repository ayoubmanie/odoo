# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'novelis theme',
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
            # 'novelisTheme/static/src/css/flUhRq6tzZclQEJ-Vdg-IuiaDsNc.woff2',
            
            ("before","web/static/src/legacy/scss/primary_variables.scss",'novelisTheme/static/src/css/colors.scss'),
            ("after","web/static/src/legacy/scss/utils.scss",'novelisTheme/static/src/css/utils.scss'),
            'novelisTheme/static/src/css/main.scss'
        ],
    }
}