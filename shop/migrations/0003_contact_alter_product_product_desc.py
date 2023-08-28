# Generated by Django 4.2.3 on 2023-08-06 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_product_product_category_product_product_image_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('msgid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=50)),
                ('subject', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=10)),
                ('message', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='product_desc',
            field=models.CharField(max_length=2000),
        ),
    ]