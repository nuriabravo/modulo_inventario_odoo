# -*- coding: utf-8 -*-
{
    'name': "Gestión de inventario para Perfumería",

    'summary': """
        Módulo para gestionar el inventario de una perfumería.""",

    'description': """
        Este módulo proporciona funcionalidades para gestionar el inventario de una perfumería, incluyendo la gestión de productos, proveedores, pedidos de compra y pedidos de venta.
    """,

    'author': "Nuria, Dani y Jaume",
    'website': "https://www.SGE2324_urlFalsa.com",
    #Indicamos que es una aplicación
    'application': True,

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.5',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
