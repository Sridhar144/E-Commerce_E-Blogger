# Generated by Django 4.2.3 on 2023-08-08 13:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_orderupdate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderupdate',
            old_name='update_desc',
            new_name='update_description',
        ),
    ]
