{
    'name': "EnmasysProjectStudy",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",
    'sequence': 2,
    'description': """
        Task 1.2
    """,

    'author': "Phat",
    'website': "http://www.enmasys.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': '',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/users_views.xml',
        'views/project_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}