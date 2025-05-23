# Generated by Django 4.0.2 on 2023-09-21 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_brand_options_alter_category_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AddField(
            model_name='product',
            name='count',
            field=models.PositiveIntegerField(default=1, help_text='Count of product'),
        ),
    ]
