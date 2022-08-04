# Generated by Django 3.2 on 2022-08-04 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_alter_order_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(blank=True, choices=[('INICIADA', 'INICIADA'), ('CANCELADA', 'CANCELADA'), ('SURTIDA', 'SURTIDA')], default='INICIADA', max_length=120),
        ),
    ]
