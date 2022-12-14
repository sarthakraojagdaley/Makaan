# Generated by Django 4.1.1 on 2022-10-21 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0051_shop_bhk_shop_additionalroom_shop_approved_shop_bath_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='garage',
            name='Bhk',
            field=models.IntegerField(default=2),
        ),
        migrations.AddField(
            model_name='garage',
            name='additionalroom',
            field=models.CharField(default='Room', max_length=50),
        ),
        migrations.AddField(
            model_name='garage',
            name='approved',
            field=models.CharField(default='Yes', max_length=50),
        ),
        migrations.AddField(
            model_name='garage',
            name='bath',
            field=models.IntegerField(default=2),
        ),
        migrations.AddField(
            model_name='garage',
            name='cornerprop',
            field=models.CharField(default='NO', max_length=5),
        ),
        migrations.AddField(
            model_name='garage',
            name='image1',
            field=models.FileField(default='images/v8.jpg', max_length=200, upload_to='images/Garage'),
        ),
        migrations.AddField(
            model_name='garage',
            name='image2',
            field=models.FileField(default='images/v8.jpg', max_length=200, upload_to='images/Garage'),
        ),
        migrations.AddField(
            model_name='garage',
            name='image3',
            field=models.FileField(default='images/v8.jpg', max_length=200, upload_to='images/Garage'),
        ),
        migrations.AddField(
            model_name='garage',
            name='landmark',
            field=models.CharField(default='Near Tonk Road', max_length=50),
        ),
        migrations.AddField(
            model_name='garage',
            name='rate',
            field=models.CharField(default='54216', max_length=50),
        ),
        migrations.AddField(
            model_name='garage',
            name='tokenamount',
            field=models.CharField(default='500000', max_length=50),
        ),
    ]
