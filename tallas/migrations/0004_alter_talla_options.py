# Generated by Django 3.2 on 2022-05-04 13:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tallas', '0003_talla_order'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='talla',
            options={'ordering': ['order']},
        ),
    ]
