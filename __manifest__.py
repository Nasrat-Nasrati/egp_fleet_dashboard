{
    'name': "EPG Fleet Dashboard",
    'version': '17.0.1.0.0',
    'category': 'Extra Tools',
    'summary': """Get a visual report of Fleet through a Dashboard in Fleet """,
    'sequence':-3,
    'description': """Fleet dashboard module brings a multipurpose graphical
     dashboard for Fleet module and making the relationship management 
     better and easier""",
    'author': 'Nasrat Nasrati member of EGP team at MCIT Kabul Afghanistan',
    'company': 'EGP team',
    'maintainer': 'EGP team',
    'website': "https://mcit.gov.af/",
    'depends': ['egp_fleet'],
    'data': [
        'views/fleet_dashboard.xml',
    ],
    'assets': {
        'web.assets_backend': [
            '/egp_fleet_dashboard/static/src/css/dashboard.css',
            '/egp_fleet_dashboard/static/src/js/dashboard.js',
            '/egp_fleet_dashboard/static/src/xml/fleet_dashboard_template.xml',
        ],
    },
    'license': 'AGPL-3',
    'installable': True,
    'application': False,
    'auto_install': False,
}
