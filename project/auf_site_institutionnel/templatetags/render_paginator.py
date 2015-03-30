#! /usr/bin/env python
# -*- encoding: utf-8 -*-
# render_paginator.py
from django.template import Library
 
register = Library()
 
def render_paginator(context, first_last_amount=2, before_after_amount=4):
    page_obj = context['page']
    paginator = context['paginator']
    query = context['query']
    page_numbers = []
 
    # Pages before current page
    if page_obj.number > first_last_amount + before_after_amount:
        for i in range(1, first_last_amount + 1):
            page_numbers.append(i)
 
        page_numbers.append(None)
 
        for i in range(page_obj.number - before_after_amount, page_obj.number):
            page_numbers.append(i)
 
    else:
        for i in range(1, page_obj.number):
            page_numbers.append(i)
 
    # Current page and pages after current page
    if page_obj.number + first_last_amount + before_after_amount < paginator.num_pages:
        for i in range(page_obj.number, page_obj.number + before_after_amount + 1):
            page_numbers.append(i)
 
        page_numbers.append(None)
 
        for i in range(paginator.num_pages - first_last_amount + 1, paginator.num_pages + 1):
            page_numbers.append(i)
 
    else:
        for i in range(page_obj.number, paginator.num_pages + 1):
            page_numbers.append(i)
 
    return {
        'paginator': paginator,
        'page': page_obj,
        'query': query,
        'page_numbers': page_numbers
    }
 
register.inclusion_tag('search/pagination.html', takes_context=True)(render_paginator)