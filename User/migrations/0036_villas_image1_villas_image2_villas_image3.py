# Generated by Django 4.1.1 on 2022-10-21 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0035_villas_cornerprop'),
    ]

    operations = [
        migrations.AddField(
            model_name='villas',
            name='image1',
            field=models.FileField(default='images/v8.jpg', max_length=200, upload_to='images/villas'),
        ),
        migrations.AddField(
            model_name='villas',
            name='image2',
            field=models.FileField(default='images/v8.jpg', max_length=200, upload_to='images/villas'),
        ),
        migrations.AddField(
            model_name='villas',
            name='image3',
            field=models.FileField(default='images/v8.jpg', max_length=200, upload_to='images/villas'),
        ),
    ]
