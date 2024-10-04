# Generated by Django 5.1 on 2024-10-03 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('product_name',), 'permissions': [('can_edit_product_description', 'can edit product description'), ('can_edit_category', 'can edit category')], 'verbose_name': 'продукт', 'verbose_name_plural': 'продукты'},
        ),
        migrations.AlterModelOptions(
            name='release',
            options={'ordering': ('version_name',), 'permissions': [('can_edit_is_active', 'can cancel publication'), ('can_edit_version', 'can edit version')], 'verbose_name': 'версия', 'verbose_name_plural': 'версии'},
        ),
        migrations.AlterField(
            model_name='release',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
