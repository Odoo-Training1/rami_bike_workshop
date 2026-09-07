{
    'name': 'Bike Workshop',
    'version': '19.0.1.5',
    'category': 'Operations',
    'summary': 'Manage bikes for rental operations',
    'depends': ['base'],
    'data': [
       'security/bike_security.xml',
        'security/ir.model.access.csv',
        'views/bike_views.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}