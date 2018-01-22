# -*- coding: utf-8 -*-
{
    'name': "sce_matrix",

    'summary': """
        Internal cube & matrix supporting,
        For multi-demetion systems."""

    'description': """
        Lots of systems, could be designed as multi-demetion system.
        which has cubes in it, and show data as matrixs in forms.
        This plugin adds internal cube model and matrix widgets.
        With which programmers can easly use cube & matrix in their
        systems.
    """,

    'author': "Jin Zan",
    'website': "http://www.sce-re.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
}
