# Generated by Django 5.0.13 on 2025-07-29 12:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='roles',
            new_name='role',
        ),
    ]
