INSTALLED_APPS += (
    'project.aldryn_search',
    'haystack',
    'spurl',
)

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'xapian_backend.XapianEngine',
        'PATH': os.path.join(PROJECT_ROOT, 'xapian_index')
    },
}

HAYSTACK_XAPIAN_LANGUAGE = "french"

#HAYSTACK_ROUTERS = ['project.aldryn_search.router.LanguageRouter',]
ALDRYN_SEARCH_INDEX_BASE_CLASS = 'project.djangocms_bureaux.search_indexes.AufIndex'
