# Generated by Django 3.2 on 2022-06-23 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categorias', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='code',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
