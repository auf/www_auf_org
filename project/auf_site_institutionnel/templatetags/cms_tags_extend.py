from cms.templatetags.cms_tags import *
from cms.templatetags.cms_tags import _show_placeholder_for_page


register = template.Library()


class PlaceholdervarNode(Placeholder):

    """This template node is used to output page content into a variable,
to allow conditional display of miscellaneous layout structures.

eg: {% placeholdervar "placeholder_name" [inherit] as varname %}
{% if varname %}
<div class="stuff">
{{ varname }}
</div>
{% endif %}
{% endplaceholdervar %}
"""

    def __init__(self, name, parser, token, var, nodelist, inherit=False):
        self.kwargs, self.blocks = self.options.parse(parser, token)
        self.name = "".join(name.lower().split('"'))
        self.var = var
        self.inherit = inherit
        self.nodelist = nodelist
        self.nodelist_or = None
        self.width = None

    def __repr__(self):
        return "<Placeholdervar Node: %s as %s>" % (self.name, self.var)

    def render_tag(self, context, name, extra_bits, nodelist=None):
        content = Placeholder.render_tag(
            self, context, name, extra_bits, nodelist)
        context.push()
        context[self.var] = mark_safe(content)
        output = self.nodelist.render(context)
        context.pop()
        return output


def do_placeholdervar(parser, token):
    error_string = '%r tag requires at least 3 and accepts at most 4 arguments'
    inherit = False
    try:
        # split_contents() knows not to split quoted strings.
        bits = token.split_contents()

        if len(bits) == 5:
            if bits[2].lower() != "inherit":
                raise template.TemplateSyntaxError(
                    "Parameter 2 must be 'inherit' when using 4 parameters")
            inherit = True

        if bits[-2].lower() != "as":
            raise template.TemplateSyntaxError(
                "Penultimate parameter must be 'as'")

        nodelist = parser.parse(('endplaceholdervar',))
        parser.delete_first_token()

    except ValueError:
        raise template.TemplateSyntaxError(error_string % bits[0])
    return PlaceholdervarNode(name=bits[1], parser=parser, token=token, var=bits[-1], nodelist=nodelist, inherit=inherit)

register.tag('placeholdervar', do_placeholdervar)


#____________________


class ShowPlaceholdervarNode(template.Node):

    """This template node is used to output page content into a variable,
to allow conditional display of miscellaneous layout structures.

eg: {% show_placeholdervar "placeholder_name" page_lookup [inherit] as varname %}
{% if varname %}
<div class="stuff">
{{ varname }}
</div>
{% endif %}
{% endshow_placeholdervar %}
"""

    def __init__(self, name, var, page_lookup, nodelist, inherit=False):
        self.name = "".join(name.lower().split('"'))
        self.var = var
        self.inherit = inherit
        self.nodelist = nodelist
        self.page_lookup = template.Variable(page_lookup)
        self.nodelist_or = None

    def __repr__(self):
        return "<ShowPlaceholdervar Node: %s as %s>" % (self.name, self.var)

    def render(self, context):
        #content = PlaceholderNode.render(self, context)
        #site = Site.objects.get_current()
        #lang = get_language_from_request(context['request'])
        content = _show_placeholder_for_page(context, self.name, self.page_lookup.resolve(
            context), lang=None, site=None, cache_result=False)['content']
        context.push()
        context[self.var] = mark_safe(content)
        output = self.nodelist.render(context)
        context.pop()
        return output


def do_show_placeholdervar(parser, token):
    error_string = '%r tag requires at least 4 and accepts at most 5 arguments'
    inherit = False
    try:
        # split_contents() knows not to split quoted strings.
        bits = token.split_contents()

        if len(bits) == 6:
            if bits[3].lower() != "inherit":
                raise template.TemplateSyntaxError(
                    "Parameter 3 must be 'inherit' when using 5 parameters")
            inherit = True

        if bits[-2].lower() != "as":
            raise template.TemplateSyntaxError(
                "Penultimate parameter must be 'as'")

        nodelist = parser.parse(('endshow_placeholdervar',))
        parser.delete_first_token()

    except ValueError:
        raise template.TemplateSyntaxError(error_string % bits[0])
    return ShowPlaceholdervarNode(name=bits[1], var=bits[-1], page_lookup=bits[2], nodelist=nodelist, inherit=inherit)
    # return ShowPlaceholdervarNode(name=bits[1], var=bits[-1], page_lookup=31, nodelist=nodelist, inherit=inherit)
    # return ShowPlaceholdervarNode(name=bits[1], var=bits[-1],
    # page_lookup=28, nodelist=nodelist, inherit=inherit)

register.tag('show_placeholdervar', do_show_placeholdervar)
