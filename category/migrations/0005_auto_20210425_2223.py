# Generated by Django 3.1 on 2021-04-25 20:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0004_auto_20210425_2214'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
        migrations.RenameField(
            model_name='category',
            old_name='category',
            new_name='category_name',
        ),
    ]
