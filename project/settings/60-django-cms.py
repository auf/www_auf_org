gettext = lambda s: s

SITE_ID = 1

MIDDLEWARE_CLASSES = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
    'pagination.middleware.PaginationMiddleware',
]

TEMPLATE_CONTEXT_PROCESSORS = [
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

    'djangocms_picture',
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

    'project.cmsplugin_pagelist',
    'project.cmsplugin_modellist',
    'project.cmsplugin_carte',
    'project.cmsplugin_bootstrap_carousel',

    'compressor',

    'adminfiles',

    'project.djangocms_bureaux',
    'project.importa',
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

TEXT_SAVE_IMAGE_FUNCTION='cmsplugin_filer_image.integrations.ckeditor.create_image_plugin'

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    #'easy_thumbnails.processors.scale_and_crop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)

#MIGRATION_MODULES = {
#    'cms': 'cms.migrations_django',
#    'menus': 'menus.migrations_django',
#    'filer': 'filer.migrations_django',
#    'cmsplugin_filer_image': 'cmsplugin_filer_image.migrations_django',
#    'cmsplugin_filer_file': 'cmsplugin_filer_file.migrations_django',
#    'cmsplugin_filer_folder': 'cmsplugin_filer_folder.migrations_django',
#    'cmsplugin_filer_link': 'cmsplugin_filer_link.migrations_django',
#    'cmsplugin_filer_teaser': 'cmsplugin_filer_teaser.migrations_django',
#    'cmsplugin_filer_utils': 'cmsplugin_filer_utils.migrations_django',
#    'cmsplugin_filer_video': 'cmsplugin_filer_video.migrations_django',
#    'djangocms_inherit': 'djangocms_inherit.migrations_django',
#    'djangocms_column': 'djangocms_column.migrations_django',
#    'djangocms_style': 'djangocms_style.migrations_django',
#    'djangocms_text_ckeditor': 'djangocms_text_ckeditor.migrations_django',
#}

CMS_TEMPLATES = (
    ('cms.html', gettext('Page du cms avec menu')),
    ('trois_colonnes.html', gettext('Trois colonnes')),
    ('deux_colonnes.html', gettext('Deux colonnes')),
    ('une_colonne.html', gettext('Une colonne')),
    ('article.html', "Article"),
    ('accueil.html', gettext('Accueil')),
)

#FILER_ENABLE_PERMISSIONS = False
#FILER_FILE_MODELS = (
#    "project.djangocms_bureaux.models.AufFile",
#    'filer.models.imagemodels.Image',
#)

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
        ['Bold', 'Italic', 'Underline', '-', 'Subscript', 'Superscript', '-', 'RemoveFormat'],
        ['JustifyLeft', 'JustifyCenter', 'JustifyRight'],
        ['HorizontalRule'],
        ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Table', 'FontAwesome'],
        ['Source']
    ],
    'toolbar_HTMLField': [
        ['Undo', 'Redo'],
        ['ShowBlocks'],
        ['Format', 'Styles'],
        ['TextColor', 'BGColor', '-', 'PasteText', 'PasteFromWord'],
        ['Maximize', ''],
        '/',
        ['Bold', 'Italic', 'Underline', '-', 'Subscript', 'Superscript', '-', 'RemoveFormat'],
        ['JustifyLeft', 'JustifyCenter', 'JustifyRight'],
        ['HorizontalRule'],
        ['Link', 'Unlink'],
        ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Table'],
        ['Source']
    ],

    'allowedContent': True,
    'toolbarCanCollapse': Talse,
    'extraPlugins': 'cmsplugins',
}
