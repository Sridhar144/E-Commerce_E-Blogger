# Generated by Django 4.2.3 on 2023-08-08 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_rename_update_desc_orderupdate_update_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderupdate',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
