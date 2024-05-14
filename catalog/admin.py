from django.contrib import admin

from catalog.models import SubCatalog, CatalogItem


@admin.register(SubCatalog)
class SubCatalogAdmin(admin.ModelAdmin):
    list_display = ('name', 'label', 'img')


@admin.register(CatalogItem)
class DiagnosticAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'main_photo')
    search_fields = ('name',)
