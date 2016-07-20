# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from django.db.models import ForeignKey
from django.db.models.fields.related import ManyToManyField
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from djangocms_blog.models import BasePostPlugin, Post, BlogCategory
from smart_selects.db_fields import ChainedManyToManyField, ChainedForeignKey


@python_2_unicode_compatible
class SingleEntry(BasePostPlugin):

    class Meta:
        managed = False

    category = ForeignKey(BlogCategory, verbose_name=_('category'))
    post = ChainedManyToManyField(
        Post,
        chained_field="category",
        chained_model_field="categories"
    )

    def __str__(self):
        return self.safe_translation_getter('single entry', any_language=True)

    def get_post(self):
        return self.post
