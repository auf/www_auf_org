INSTALLED_APPS += (
    'standard_form',
    'aldryn_search',
    'haystack',
)

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': os.path.join(PROJECT_ROOT, 'whoosh_index'),
        'INCLUDE_SPELLING': True,
    },
}

HAYSTACK_ROUTERS = ['aldryn_search.router.LanguageRouter',]

