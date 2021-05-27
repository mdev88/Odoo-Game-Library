{
    'name': "Game Library",
    'version': '1.0',
    'depends': [],
    'author': "M",
    'sequence': 10,
    'category': 'Category',
    'installable': True,
    'application': True,
    'description': """
    Game Library
    """,
    # data files always loaded at installation
    'data': [
        'security/ir.model.access.csv',
        'views/game.xml',
    ],
    # data files containing optionally loaded demonstration data
    'demo': [
        # 'demo/testdemo_data.xml',
    ],
}