# -*- encoding: utf-8 -*-
from django.contrib.admin.filterspecs import FilterSpec


class EtablissementFilterSpec(FilterSpec):

    def __init__(self, f, request, params, model, model_admin, field_path=None):
        super(EtablissementFilterSpec, self).__init__(
            f, request, params, model, model_admin, field_path=field_path)

        self.filtered_fields = frozenset(('validation_etablissement',
                                          'a_valider_sai',
                                          'a_valider_com',
                                          'validation_sai',
                                          'validation_com',))

        self.params = dict([(k, v) for k, v in params.items()
                            if k in self.filtered_fields
                            ])
        self.links = (
            (u'Tous', {}),
            (u'En attente', {u'validation_etablissement': u'0'}),
            (u'À valider SAI', {u'a_valider_sai': u'1'}),
            (u'À valider COM', {u'a_valider_com': u'1'}),
            (u'Complets', {u'validation_sai': u'1', u'validation_com': u'1'}),

        )

    def title(self):
        return u"validation"

    def choices(self, cl):
        for label, conditions_dict in self.links:
            yield {'selected': self.params == conditions_dict,
                   'query_string': cl.get_query_string(
                       conditions_dict,
                       self.filtered_fields.difference(conditions_dict.keys())),
                   'display': label
                   }

FilterSpec.filter_specs.insert(0, (lambda f: getattr(
    f, 'validation_sai_com_filter', False), EtablissementFilterSpec))
