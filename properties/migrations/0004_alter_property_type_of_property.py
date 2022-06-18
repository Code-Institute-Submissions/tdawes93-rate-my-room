# Generated by Django 3.2.13 on 2022-06-17 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0003_auto_20220617_1914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='type_of_property',
            field=models.CharField(choices=[('1', 'Flat'), ('2', 'Terrace house'), ('3', 'Semi-detached house'), ('4', 'Detached house'), ('5', 'Bungalow'), ('6', 'House share')], default=1, max_length=30),
        ),
    ]