# Generated by Django 5.0.1 on 2024-01-05 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockdb',
            name='closing_price',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='stockdb',
            name='opening_price',
            field=models.FloatField(),
        ),
    ]
