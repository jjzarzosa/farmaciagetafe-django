# Generated by Django 3.1 on 2021-04-25 13:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='apodo',
            new_name='username',
        ),
    ]
