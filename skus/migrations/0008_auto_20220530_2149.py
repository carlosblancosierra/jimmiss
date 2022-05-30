# Generated by Django 3.2 on 2022-05-30 21:49

from django.db import migrations
import imagekit.models.fields
import skus.models


class Migration(migrations.Migration):

    dependencies = [
        ('skus', '0007_auto_20220530_2024'),
    ]

    operations = [
        migrations.AddField(
            model_name='skumaster',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to=skus.models.upload_location),
        ),
        migrations.AddField(
            model_name='skumaster',
            name='image_2',
            field=imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to=skus.models.upload_location),
        ),
        migrations.AddField(
            model_name='skumaster',
            name='image_3',
            field=imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to=skus.models.upload_location),
        ),
        migrations.AddField(
            model_name='skumaster',
            name='image_4',
            field=imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to=skus.models.upload_location),
        ),
        migrations.AddField(
            model_name='skumaster',
            name='image_5',
            field=imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to=skus.models.upload_location),
        ),
    ]
