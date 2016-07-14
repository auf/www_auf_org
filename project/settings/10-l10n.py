# -*- encoding: utf-8 -*-

TIME_ZONE = 'America/Montreal'

LANGUAGE_CODE = 'fr'

gettext = lambda s: s

LANGUAGES = (
    ('fr', gettext(u'french')),
)

USE_I18N = True
USE_L10N = True
USE_TZ = False
