# Generated by Django 4.1.1 on 2022-10-21 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0046_building_bhk_building_additionalroom_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='building',
            name='image1',
            field=models.FileField(default='images/v8.jpg', max_length=200, upload_to='images/Building'),
        ),
        migrations.AlterField(
            model_name='building',
            name='image2',
            field=models.FileField(default='images/v8.jpg', max_length=200, upload_to='images/Building'),
        ),
        migrations.AlterField(
            model_name='building',
            name='image3',
            field=models.FileField(default='images/v8.jpg', max_length=200, upload_to='images/Building'),
        ),
    ]
