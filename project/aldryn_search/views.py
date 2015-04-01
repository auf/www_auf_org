# -*- coding: utf-8 -*-
import re

from django.utils.translation import get_language_from_request
from django.views.generic import ListView
from django.views.generic.edit import FormMixin

from django import forms

from haystack.forms import ModelSearchForm
from haystack.forms import FacetedSearchForm
from haystack.query import SearchQuerySet


from aldryn_common.paginator import DiggPaginator

from .conf import settings
from .utils import alias_from_language, get_model_path


class AldrynFacetedSearchForm(FacetedSearchForm):
    selected_facets = forms.CharField(required=False, widget=forms.HiddenInput)

    def search(self):
        if self.is_valid():
            if self.cleaned_data.get('q', ''):
                sqs = SearchQuerySet().auto_query(self.cleaned_data['q'])
            else:
                sqs = SearchQuerySet().exclude(content='cettechaineneserapastrouve')
        else:
            sqs = SearchQuerySet().exclude(content='cettechaineneserapastrouve')

        sqs = sqs.facet('bureaux').facet('section').facet('annee')

        for facet in self.selected_facets:
            if "__" not in facet:
                continue

            field, value = facet.split("__", 1)

            if value:
                sqs = sqs.narrow(u'%s:"%s"' % (field, sqs.query.clean(value)))

        return sqs


class AldrynSearchView(FormMixin, ListView):
    form_class = AldrynFacetedSearchForm

    paginate_by = settings.ALDRYN_SEARCH_PAGINATION
    paginator_class = DiggPaginator

    template_name = 'aldryn_search/search_results.html'

    def get(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        self.form = self.get_form(form_class)
        return super(AldrynSearchView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        self.queryset = self.form.search()
        if not self.request.user.is_authenticated():
            self.queryset = self.queryset.exclude(login_required=True)
        return self.queryset

    def get_context_data(self, **kwargs):
        context = super(AldrynSearchView, self).get_context_data(**kwargs)

        q = self.form.search()
        if not self.request.user.is_authenticated():
            q = q.exclude(login_required=True)

        context['form'] = self.form
        context['facets'] = self.queryset.facet_counts()
        context['selected_facets'] = self.request.GET.getlist('selected_facets', [])
        if self.object_list.query.backend.include_spelling:
            context['suggestion'] = self.form.get_suggestion()
        return context
