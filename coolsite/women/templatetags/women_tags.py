from django import template
from django.http import Http404
from women.models import Women, Category


register = template.Library()


@register.simple_tag(name='getcats')
def get_categories(filter=None):
    """Пример использования простого тeга"""
    if not filter:
        return Category.objects.all()
    else:
        return Category.objects.filter(pk=filter)


@register.inclusion_tag('women/template_for_tags/list_categories.html')
def show_categories(sort=None, cat_selected=0):
    """Пример использования включающего тeга"""
    if not sort:
        cats = Category.objects.all()
    else:
        cats = Category.objects.order_by(sort)

    return {'cats': cats, 'cat_selected': cat_selected}


# @register.inclusion_tag('women/template_for_tags/list_posts.html')
# def show_posts(cat_selected=0):
#     if not cat_selected or cat_selected == 0:
#         posts = Women.objects.filter(is_published=True)
#         return {'posts': posts}
#     else:
#         posts = Women.objects.filter(cat_id=cat_selected).filter(is_published=True)
#         if len(posts) == 0:
#             raise Http404
#         return {'posts': posts, 'cat_selected': cat_selected}
