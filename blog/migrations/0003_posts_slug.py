# Generated by Django 4.2.3 on 2023-08-13 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_posts'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='slug',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]