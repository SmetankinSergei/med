from django import template

from catalog.models import SubCatalog, CatalogItem

register = template.Library()


@register.simple_tag()
def get_sub_catalogs():
    return SubCatalog.objects.all()


@register.simple_tag()
def get_catalog_items(sub_catalog_name):
    sub_catalog_id = SubCatalog.objects.get(name=sub_catalog_name).pk
    return CatalogItem.objects.filter(sub_catalog=sub_catalog_id)


@register.simple_tag()
def main_photo_path_tag(item):
    return item.main_photo.url


@register.filter()
def main_photo_path(item_photo_path):
    return item_photo_path.url
