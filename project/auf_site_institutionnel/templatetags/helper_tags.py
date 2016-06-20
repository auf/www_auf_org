# coding=utf-8
from django.template import Library
from django.conf import settings
register = Library()


@register.simple_tag
def template_dir(obj):
    if settings.DEBUG:
        output = dir(obj)
        return "<pre>" + str(output) + "</pre>"
    return ""


@register.simple_tag
def estampilles(values):
    bureaux = {
        'Amériques': 'BA',
        'Afrique centrale et des Grands-Lacs': 'BACGL',
        'Afrique de l\'Ouest': 'BAO',
        'Asie-Pacifique': 'BAP',
        'Caraïbe': 'BC',
        'Europe centrale et orientale': 'BECO',
        'Europe de l\'Ouest': 'BEO',
        'Moyen-Orient': 'BMO',
        'Maghreb': 'BM',
        'Océan Indien': 'BOI'
    }
    output = []

    for tag in values:
        tag = str(tag)
        if tag == "International":
            output.append("<i class=\"fa fa-globe\">-International</i>")
        else:
            if tag in bureaux:
                output.append("<i class=\"fa fa-circle " + bureaux[tag] + " data-toggle=\"popover\" data-content=\"<a href='/" +
                              bureaux[tag] + "'>" + tag + "</a>\" data-placement=\"top\" data-trigger=\"focus\" " +
                              "tabindex=\"0\" data-original-title=\"\" title=\"\">-" + bureaux[tag] + "</i>")

    output = ''.join(output)
    return '<div class="mini-estampilles">' + output + '</div>'
