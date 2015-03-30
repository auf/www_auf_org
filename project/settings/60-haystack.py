INSTALLED_APPS += (
    'project.aldryn_search',
    'haystack',
    'spurl',
)

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': os.path.join(PROJECT_ROOT, 'whoosh_index'),
        'INCLUDE_SPELLING': True,
    },
}

#HAYSTACK_ROUTERS = ['project.aldryn_search.router.LanguageRouter',]
ALDRYN_SEARCH_INDEX_BASE_CLASS= 'project.djangocms_bureaux.search_indexes.AufIndex'
