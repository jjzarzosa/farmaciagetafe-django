# Generated by Django 3.1 on 2021-04-25 20:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210425_1544'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='apellidos',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='account',
            old_name='nombre',
            new_name='last_name',
        ),
    ]
