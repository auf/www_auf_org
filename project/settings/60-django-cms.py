gettext = lambda s: s
_ = lambda s: s

SITE_ID = 1

MIDDLEWARE_CLASSES = [
    'django.middleware.cache.UpdateCacheMiddleware',
# FIXME
#    'cms.middleware.utils.ApphookReloadMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'auf.django.saml.middleware.SPMiddleware',
    'auf.django.piwik.middleware.TrackMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
    'pagination.middleware.PaginationMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
]


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(PROJECT_ROOT, "templates/"),
        ],
        'OPTIONS': {
            'context_processors': [
             "django.contrib.auth.context_processors.auth",
             "django.contrib.messages.context_processors.messages",
             "django.core.context_processors.i18n",
             "django.core.context_processors.debug",
             "django.core.context_processors.request",
             "django.core.context_processors.media",
             'django.core.context_processors.csrf',
             "django.core.context_processors.tz",
             "sekizai.context_processors.sekizai",
             "django.core.context_processors.static",
             "cms.context_processors.cms_settings",
              ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ],
          },
     },
]


INSTALLED_APPS = ('djangocms_admin_style',) + INSTALLED_APPS

INSTALLED_APPS += (
    # CMS related apps
    'cms',
    'treebeard',
    'menus',
    'django_extensions',

    'reversion',
    'sekizai',
    'filer',
    'easy_thumbnails',
    'cmsplugin_filer_file',
    'cmsplugin_filer_folder',
    'cmsplugin_filer_image',
    'cmsplugin_filer_link',
    'cmsplugin_filer_teaser',
    'cmsplugin_filer_utils',
    'cmsplugin_filer_video',

    #'cmsplugin_embeddedmenu',
    'cmsplugin_tabs',

    'djangocms_inherit',
    'djangocms_style',
    'djangocms_text_ckeditor',

    'aldryn_apphooks_config',
    'djangocms_blog',

    'parler',
    'taggit',
    'taggit_autosuggest',
    'django_select2',
    'meta',
    'meta_mixin',
    'admin_enhancer',

    'project.cmsplugin_carte',
    'project.cmsplugin_bootstrap_carousel',
    'project.cmsplugin_mailman',

    'compressor',

    'adminfiles',

    'project.importa',
    'adminsortable',
)

LANGUAGES = [
    ('fr', gettext('French')),
]
CMS_LANGUAGES = LANGUAGES

CMS_LANGUAGES = {
    1: [
        {
            'code': 'fr',
            'name': gettext('Francais'),
            'public': True,
        },
    ],
}


CMS_URL_OVERWRITE = True
CMS_MENU_TITLE_OVERWRITE = True
CMS_REDIRECTS = True
CMS_SOFTROOT = True
CMS_SHOW_START_DATE = True
CMS_SHOW_END_DATE = True
CMS_SEO_FIELDS = True
CMS_PERMISSION = True
CMS_PUBLIC_FOR = 'all'

TEXT_SAVE_IMAGE_FUNCTION = 'cmsplugin_filer_image.integrations.ckeditor.create_image_plugin'

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    #'easy_thumbnails.processors.scale_and_crop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)

CMS_TEMPLATES = (
    ('cms.html', gettext('Page du cms avec menu')),
    ('breves2.html', gettext('Breves2')),
    ('newsletter/fil.html', gettext('Fil')),
    ('newsletter/lettre.html', gettext('Lettre')),
    ('newsletter/planete.html', gettext('Planete')),
    ('lettres.html', gettext('lettres interne')),
    ('content_menu.html', gettext('Page menu')),
    ('trois_colonnes.html', gettext('Trois colonnes')),
    ('deux_colonnes.html', gettext('Deux colonnes')),
    ('une_colonne.html', gettext('Une colonne')),
    ('article.html', "Article"),
    ('accueil.html', gettext('Accueil')),
)

#FILER_ENABLE_PERMISSIONS = False
# FILER_FILE_MODELS = (
#    "project.djangocms_bureaux.models.AufFile",
#    'filer.models.imagemodels.Image',
#)

META_SITE_PROTOCOL = 'http'
META_USE_SITES = True

BLOG_ENABLE_COMMENTS = False
BLOG_USE_PLACEHOLDER = True

BLOG_PLUGIN_TEMPLATE_FOLDERS = (
    ('plugins', _('Default template')),
    ('mini', _('Mini')),
)

PERMALINKS = (
    ('full_date', _('Full date')),
    ('short_date', _('Year /  Month')),
    ('slug', _('Just slug')),
)

PERMALINKS_URLS = {
    'full_date': r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/(?P<slug>\w[-\w]*)/$',
    'short_date': r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<slug>\w[-\w]*)/$',
    'slug': r'^(?P<slug>\w[-\w]*)/$',
}

CKEDITOR_SETTINGS = {
    'contentsCss': '/static/css/font-awesome.min.css',
    'extraPlugins': 'fontawesome',
    'allowedContent': True,

    'language': '{{ language }}',
    'skin': 'moono',
    'toolbar_CMS': [
        ['Undo', 'Redo'],
        ['cmsplugins', '-', 'ShowBlocks'],
        ['Format', 'Styles'],
        ['TextColor', 'BGColor', '-', 'PasteText', 'PasteFromWord'],
        ['Maximize', ''],
        '/',
        ['Bold', 'Italic', 'Underline', '-', 'Subscript',
            'Superscript', '-', 'RemoveFormat'],
        ['JustifyLeft', 'JustifyCenter', 'JustifyRight'],
        ['HorizontalRule'],
        ['NumberedList', 'BulletedList', '-',
            'Outdent', 'Indent', '-', 'Table'],
        ['FontAwesome'],
        ['Breve'],
        ['Source']
    ],
    'toolbar_HTMLField': [
        ['Undo', 'Redo'],
        ['ShowBlocks'],
        ['Format', 'Styles'],
        ['TextColor', 'BGColor', '-', 'PasteText', 'PasteFromWord'],
        ['Maximize', ''],
        '/',
        ['Bold', 'Italic', 'Underline', '-', 'Subscript',
            'Superscript', '-', 'RemoveFormat'],
        ['JustifyLeft', 'JustifyCenter', 'JustifyRight'],
        ['HorizontalRule'],
        ['Link', 'Unlink'],
        ['NumberedList', 'BulletedList', '-',
            'Outdent', 'Indent', '-', 'Table'],
        ['Source']
    ],

    'allowedContent': True,
    'toolbarCanCollapse': False,
    'extraPlugins': 'cmsplugins,fontawesome,auf',
}
