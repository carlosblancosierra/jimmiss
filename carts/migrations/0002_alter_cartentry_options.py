# Generated by Django 3.2 on 2022-08-30 22:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cartentry',
            options={'ordering': ['sku_product']},
        ),
    ]