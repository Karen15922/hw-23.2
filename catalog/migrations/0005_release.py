# Generated by Django 5.0.3 on 2024-09-17 21:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_rename_product_category_product_category_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Release',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.DecimalField(decimal_places=2, help_text='Введите версию продукта', max_digits=4, verbose_name='Версия')),
                ('version_name', models.CharField(blank=True, help_text='Введите название версии продукта', max_length=100, null=True, verbose_name='Название версии')),
                ('is_Active', models.BooleanField(default=False, verbose_name='Активная версия')),
                ('product', models.ForeignKey(default='empty', help_text='Выберте продукт', on_delete=django.db.models.deletion.CASCADE, to='catalog.product', verbose_name='Продукт')),
            ],
            options={
                'verbose_name': 'версия',
                'verbose_name_plural': 'версии',
                'ordering': ('version_name',),
            },
        ),
    ]
