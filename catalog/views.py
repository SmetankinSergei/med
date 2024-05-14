from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic import TemplateView

from catalog.constants import SUB_CATALOG_CONTEXT
from catalog.models import CatalogItem
from catalog.templatetags.catalog_tags import get_catalog_items


def catalog(request):
    return render(request, 'catalog/catalog.html')


class Catalog(TemplateView):
    template_name = 'catalog/catalog.html'


def sub_catalog(request, sub_catalog_name, current_item_type, prev_item_type):
    page = request.GET.get('page', 1)
    items = get_catalog_items(sub_catalog_name)
    paginator = Paginator(items, 6)
    current_page = paginator.page(int(page))
    print(items)
    context = {
        'sub_catalog_name': sub_catalog_name,
        'current_item_type': current_item_type,
        'prev_item_type': prev_item_type,
        'items': current_page,
    }
    return render(request, 'catalog/sub_catalog.html', {**context, **SUB_CATALOG_CONTEXT})


def item(request, item_id, sub_catalog_name):
    catalog_item = CatalogItem.objects.get(pk=item_id)
    context = {'item': catalog_item}
    return render(request, 'catalog/catalog_item.html', {**context, **SUB_CATALOG_CONTEXT})
