# -*- coding: utf-8 -*-
from djangocms_blog.forms import LatestEntriesForm


class AUFLatestEntriesForm(LatestEntriesForm):
    class Meta:
        exclude = ["categories"]
