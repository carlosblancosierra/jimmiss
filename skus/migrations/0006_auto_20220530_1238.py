# Generated by Django 3.2 on 2022-05-30 12:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('divisiones', '0001_initial'),
        ('series', '0001_initial'),
        ('marcas', '0001_initial'),
        ('composiciones', '0001_initial'),
        ('skus', '0005_skuproduct_sku'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skuproduct',
            name='composicion',
        ),
        migrations.RemoveField(
            model_name='skuproduct',
            name='division',
        ),
        migrations.RemoveField(
            model_name='skuproduct',
            name='marca',
        ),
        migrations.RemoveField(
            model_name='skuproduct',
            name='serie',
        ),
        migrations.AddField(
            model_name='skumaster',
            name='composicion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='composicion_skuproduct_set', to='composiciones.composicion'),
        ),
        migrations.AddField(
            model_name='skumaster',
            name='division',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='division_skuproduct_set', to='divisiones.division'),
        ),
        migrations.AddField(
            model_name='skumaster',
            name='marca',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='marca_skuproduct_set', to='marcas.marca'),
        ),
        migrations.AddField(
            model_name='skumaster',
            name='serie',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='serie_skuproduct_set', to='series.serie'),
        ),
    ]
