# Generated by Django 4.1.1 on 2022-10-21 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0023_building_detail_garage_detail_house_detail_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='villas',
            name='Bhk',
            field=models.IntegerField(default=2),
        ),
    ]
