# Generated by Django 4.1.1 on 2022-10-22 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0057_villas_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Addproperty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ptype', models.CharField(max_length=50)),
                ('typeof', models.CharField(max_length=50)),
                ('price', models.IntegerField(default=6)),
                ('location', models.CharField(max_length=50)),
                ('city', models.CharField(default='Jaipur', max_length=50)),
                ('area', models.CharField(max_length=50)),
                ('bed', models.IntegerField()),
                ('bath', models.IntegerField()),
                ('image1', models.FileField(default='images/v8.jpg', max_length=200, upload_to='images/AddProperties')),
                ('image2', models.FileField(default='images/v8.jpg', max_length=200, upload_to='images/AddProperties')),
                ('image3', models.FileField(default='images/v8.jpg', max_length=200, upload_to='images/AddProperties')),
                ('Bhk', models.IntegerField(default=2)),
                ('approved', models.CharField(default='Yes', max_length=50)),
                ('landmark', models.CharField(default='Near Tonk Road', max_length=50)),
                ('floors', models.IntegerField(default=3)),
                ('status', models.CharField(default='Fresh', max_length=50)),
                ('rate', models.CharField(default='54216', max_length=50)),
                ('tokenamount', models.CharField(default='500000', max_length=50)),
                ('additionalroom', models.CharField(default='Room', max_length=50)),
                ('cornerprop', models.CharField(default='NO', max_length=5)),
                ('youare', models.CharField(default='Agent', max_length=50)),
                ('saletype', models.CharField(default='Fresh', max_length=50)),
                ('facing', models.CharField(default='East', max_length=50)),
                ('roadwidth', models.IntegerField(default=20)),
                ('locality', models.CharField(default='Kumbha Marg', max_length=50)),
                ('contactdetail', models.CharField(default='7698679876', max_length=50)),
                ('altcontact', models.CharField(default='8778986745', max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='apartments',
            name='altcontact',
        ),
        migrations.RemoveField(
            model_name='apartments',
            name='contactdetail',
        ),
        migrations.RemoveField(
            model_name='apartments',
            name='facing',
        ),
        migrations.RemoveField(
            model_name='apartments',
            name='locality',
        ),
        migrations.RemoveField(
            model_name='apartments',
            name='roadwidth',
        ),
        migrations.RemoveField(
            model_name='apartments',
            name='saletype',
        ),
        migrations.RemoveField(
            model_name='apartments',
            name='youare',
        ),
        migrations.RemoveField(
            model_name='building',
            name='altcontact',
        ),
        migrations.RemoveField(
            model_name='building',
            name='contactdetail',
        ),
        migrations.RemoveField(
            model_name='building',
            name='facing',
        ),
        migrations.RemoveField(
            model_name='building',
            name='locality',
        ),
        migrations.RemoveField(
            model_name='building',
            name='roadwidth',
        ),
        migrations.RemoveField(
            model_name='building',
            name='saletype',
        ),
        migrations.RemoveField(
            model_name='building',
            name='youare',
        ),
        migrations.RemoveField(
            model_name='garage',
            name='altcontact',
        ),
        migrations.RemoveField(
            model_name='garage',
            name='contactdetail',
        ),
        migrations.RemoveField(
            model_name='garage',
            name='facing',
        ),
        migrations.RemoveField(
            model_name='garage',
            name='locality',
        ),
        migrations.RemoveField(
            model_name='garage',
            name='roadwidth',
        ),
        migrations.RemoveField(
            model_name='garage',
            name='saletype',
        ),
        migrations.RemoveField(
            model_name='garage',
            name='youare',
        ),
        migrations.RemoveField(
            model_name='house',
            name='altcontact',
        ),
        migrations.RemoveField(
            model_name='house',
            name='contactdetail',
        ),
        migrations.RemoveField(
            model_name='house',
            name='facing',
        ),
        migrations.RemoveField(
            model_name='house',
            name='locality',
        ),
        migrations.RemoveField(
            model_name='house',
            name='roadwidth',
        ),
        migrations.RemoveField(
            model_name='house',
            name='saletype',
        ),
        migrations.RemoveField(
            model_name='house',
            name='youare',
        ),
        migrations.RemoveField(
            model_name='office',
            name='altcontact',
        ),
        migrations.RemoveField(
            model_name='office',
            name='contactdetail',
        ),
        migrations.RemoveField(
            model_name='office',
            name='facing',
        ),
        migrations.RemoveField(
            model_name='office',
            name='locality',
        ),
        migrations.RemoveField(
            model_name='office',
            name='roadwidth',
        ),
        migrations.RemoveField(
            model_name='office',
            name='saletype',
        ),
        migrations.RemoveField(
            model_name='office',
            name='youare',
        ),
        migrations.RemoveField(
            model_name='shop',
            name='altcontact',
        ),
        migrations.RemoveField(
            model_name='shop',
            name='contactdetail',
        ),
        migrations.RemoveField(
            model_name='shop',
            name='facing',
        ),
        migrations.RemoveField(
            model_name='shop',
            name='locality',
        ),
        migrations.RemoveField(
            model_name='shop',
            name='roadwidth',
        ),
        migrations.RemoveField(
            model_name='shop',
            name='saletype',
        ),
        migrations.RemoveField(
            model_name='shop',
            name='youare',
        ),
        migrations.RemoveField(
            model_name='townhouse',
            name='altcontact',
        ),
        migrations.RemoveField(
            model_name='townhouse',
            name='contactdetail',
        ),
        migrations.RemoveField(
            model_name='townhouse',
            name='facing',
        ),
        migrations.RemoveField(
            model_name='townhouse',
            name='locality',
        ),
        migrations.RemoveField(
            model_name='townhouse',
            name='roadwidth',
        ),
        migrations.RemoveField(
            model_name='townhouse',
            name='saletype',
        ),
        migrations.RemoveField(
            model_name='townhouse',
            name='youare',
        ),
        migrations.RemoveField(
            model_name='villas',
            name='altcontact',
        ),
        migrations.RemoveField(
            model_name='villas',
            name='contactdetail',
        ),
        migrations.RemoveField(
            model_name='villas',
            name='facing',
        ),
        migrations.RemoveField(
            model_name='villas',
            name='locality',
        ),
        migrations.RemoveField(
            model_name='villas',
            name='roadwidth',
        ),
        migrations.RemoveField(
            model_name='villas',
            name='saletype',
        ),
        migrations.RemoveField(
            model_name='villas',
            name='youare',
        ),
    ]
