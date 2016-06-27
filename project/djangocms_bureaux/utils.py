# -*- coding: utf-8 -*-
from djangocms_blog.models import BlogCategory


def get_auf_post_categories():
    categories = BlogCategory.objects.language('fr').all()
    category_ids = {}

    for category in categories:
        if category.slug == 'actualites':
            category_ids['Actualite'] = category.id
        elif category.slug == 'allocations':
            category_ids['Bourse'] = category.id
        elif category.slug == 'appels-offre':
            category_ids['Appel_Offre'] = category.id
        elif category.slug == 'evenements':
            category_ids['Evenement'] = category.id
        elif category.slug == 'publications':
            category_ids['Publication'] = category.id
    return category_ids


def get_auf_post_category(category):
    categories = get_auf_post_categories()
    return BlogCategory.objects.language('fr').get(id=categories[category])
