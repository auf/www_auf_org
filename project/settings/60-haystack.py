INSTALLED_APPS += (
    'standard_form',
    'aldryn_search',
    'haystack',
)

HAYSTACK_CONNECTIONS = {
    'fr': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': os.path.join(PROJECT_ROOT, 'whoosh_index'),
        'INCLUDE_SPELLING': True,
    },
}

HAYSTACK_ROUTERS = ['aldryn_search.router.LanguageRouter',]
HAYSTACK_CONNECTIONS['default'] = HAYSTACK_CONNECTIONS['fr']
ALDRYN_SEARCH_INDEX_BASE_CLASS= 'project.djangocms_bureaux.search_indexes.AufIndex'
