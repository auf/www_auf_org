from django.template import Library
from django.conf import settings
register = Library()


@register.simple_tag
def template_dir(obj):
    if settings.DEBUG:
        output = dir(obj)
        return "<pre>" + str(output) + "</pre>"
    return ""
