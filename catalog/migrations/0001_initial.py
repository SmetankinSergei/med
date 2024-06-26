# Generated by Django 5.0.6 on 2024-05-12 18:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SubCatalog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Name')),
                ('label', models.CharField(max_length=20, verbose_name='Label')),
                ('img', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Sub catalog',
                'verbose_name_plural': 'Sub catalogs',
                'ordering': ('-name',),
            },
        ),
        migrations.CreateModel(
            name='Procedure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('main_photo', models.ImageField(upload_to='parts_img/')),
                ('sub_catalog', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='part_sub_catalog', to='catalog.subcatalog')),
            ],
            options={
                'verbose_name': 'Part',
                'verbose_name_plural': 'Parts',
                'ordering': ('pk',),
            },
        ),
        migrations.CreateModel(
            name='Diagnostic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('main_photo', models.ImageField(upload_to='diagnostics_img/')),
                ('sub_catalog', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='diagnostic_sub_catalog', to='catalog.subcatalog')),
            ],
            options={
                'verbose_name': 'Diagnostic',
                'verbose_name_plural': 'Diagnostics',
                'ordering': ('pk',),
            },
        ),
    ]
