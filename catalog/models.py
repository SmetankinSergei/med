from django.db import models
from django.db.models import PROTECT


NULLABLE = {'null': True, 'blank': True}


class SubCatalog(models.Model):
    name = models.CharField(max_length=20, verbose_name='Name')
    label = models.CharField(max_length=20, verbose_name='Label')
    img = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Sub catalog'
        verbose_name_plural = 'Sub catalogs'
        ordering = ('-name',)


class CatalogItem(models.Model):

    name = models.CharField(max_length=50)
    price = models.IntegerField()
    sub_catalog = models.ForeignKey('SubCatalog', on_delete=PROTECT, related_name='diagnostic_sub_catalog')
    main_photo = models.ImageField(upload_to='diagnostics_img/')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Catalog item'
        verbose_name_plural = 'Catalog items'
        ordering = ('pk',)
