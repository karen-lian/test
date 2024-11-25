{
    'name': 'IDX_TEST_測驗模組',
    'version': '1.0',
    'category': 'ideaXpress/ideaXpress',
    'summary': 'IDX_TEST_測驗模組',
    'description': 'IDX_TEST_測驗模組',
    'author': 'Karen',
    'license': 'LGPL-3',
    'depends': ['base', 'purchase'],
    'data': [
        'data/ir_sequence_data.xml',

        'views/group_buying.xml',
        'views/purchase_order_views.xml',
        'views/menu_views.xml',

        'security/security.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
