# -*- coding: utf-8 -*-
# //////////////////////////////////////////////////////////////////////////////
#
#    Saloua SAHNOUNE.
#
#    Copyright (C) 2020-TODAY Saloua SAHNOUNE(<ssaloua.sahnoune@gmail.com>).
#    Author: Saloua SAHNOUNE, (ssaloua.sahnoune@gmail.com)
#
# //////////////////////////////////////////////////////////////////////////////

{
    'name': "Auto archive contact",
    'version': '1.0.0',
    'summary': """Automatically archive a contact once their business / client is archived .""",
    'description': """
       Automatically archive a contact once their business / client is archived . ODOO 13
    """,
    'author': 'Saloua SAHNOUNE',
    'company': 'SAHNOUNE SALOUA',
    'website': "ssaloua.sahnoune@gmail.com",
    'category': 'Sales',
    'depends': [
        'sale',
        'base'

                ],
    'data': [
        'views/res_partner.xml',
    ],
    'demo': [],
    'images': [

    ],
    'license': 'AGPL-3',
    'installable': True,
    'application': False
}


