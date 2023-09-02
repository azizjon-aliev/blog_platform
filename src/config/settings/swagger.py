SPECTACULAR_SETTINGS = {
    'TITLE': 'E-commerce API Documentation',
    'DESCRIPTION': 'Description api',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
    'COMPONENT_SPLIT_REQUEST': True,
    'SPECTACULAR_DEFAULTS': {
        'SERVE_PERMISSIONS': ['rest_framework.permissions.AllowAny'],
    },
    'SCHEMA_PATH_PREFIX': r'/api/v[0-9]',
}
