# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Cinema',
    'version' : '1.0',
    'summary': 'simple cinema management system',
    'sequence': 15,
    'description': """
simple cinema management system
    """,
    'category': '',
    'website': '',
    'images': [],
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/timetable.xml',
        'views/movie.xml',
        'views/room.xml',
        'views/menu.xml'
    ],
    'demo': [
        #'demo/account_demo.xml',
    ],
    'qweb': [

    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    #'post_init_hook': '_auto_install_l10n',
}