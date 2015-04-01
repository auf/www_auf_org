# encoding: utf-8

from django.utils.http import urlunquote, urlquote
from django import template

register = template.Library()

BUREAU_SLUGS = {
    u'/bureau/bureau-ameriques': ('BA', 'Bureaux des Amériques'),
    u'/bureau/bureau-afrique-centrale-et-des-grands-lacs': ('BACGL', 'Bureau Afrique centrale et des Grands-Lacs'),
    u'/bureau/bureau-afrique-de-l-ouest': ('BAO', 'Bureau Afrique de l\'Ouest'),
    u'/bureau/bureau-asie-pacifique': ('BAP', 'Asie-Pacifique'),
    u'/bureau/bureau-caraibe': ('BC', 'Bureau Caraïbe'),
    u'/bureau/bureau-europe-centrale-et-orientale': ('BECO', 'Bureau Europe centrale et orientale'),
    u'/bureau/bureau-europe-de-l-ouest': ('BEO', 'Bureau Europe de l\'Ouest'),
    u'/bureau/bureau-moyen-orient': ('BMO', 'Bureau Moyen-Orient'),
    u'/bureau/bureau-maghreb': ('BM', 'Bureau Maghreb'),
    u'/bureau/bureau-ocean-indien': ('BOI', 'Bureau Océan Indien'),
}


@register.assignment_tag(takes_context=True)
def get_bureau(context):
    path = context['request'].path
    for key in BUREAU_SLUGS.keys():
        if path.startswith(key):
            return BUREAU_SLUGS[key]
    return ('', '')

@register.filter
def bureaux(obj):
    bureaux = list(obj.bureau.all())
    return ', '.join([b.nom for b in bureaux]) if bureaux else 'International'


@register.simple_tag(takes_context=True, name="show_facet")
def do_show_facet(context, facet_name):
    html = ""
    facets = context['facets']['fields'][facet_name]
    selected_facets = context['selected_facets']
    get_full_path = context['request'].get_full_path()

    for f in facets:
        long_facet_name = "__".join([facet_name, urlquote(f[0])])

        if urlunquote(long_facet_name) in selected_facets:
            html += "<dd><a href='%s'>(-) %s</a> (%s)</dd>"\
                % (get_full_path.replace("&selected_facets=" + long_facet_name,""),
                   f[0], f[1])
        else:
            html += "<dd><a href='%s?&selected_facets=%s'>%s</a> (%s)</dd>"\
                % (get_full_path, long_facet_name, f[0], f[1])
    return html
