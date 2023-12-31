# Generated by Django 4.2.3 on 2023-08-08 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_contact_alter_product_product_desc'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('items_json', models.CharField(max_length=5000)),
                ('name', models.CharField(max_length=40)),
                ('email', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=400)),
                ('city', models.CharField(max_length=15)),
                ('state', models.CharField(max_length=20)),
                ('zip_code', models.CharField(max_length=11)),
            ],
        ),
    ]
