# Generated by Django 4.2.3 on 2023-08-17 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_rename_blog_blogcomment_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
