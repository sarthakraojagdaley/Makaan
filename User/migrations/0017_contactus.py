# Generated by Django 4.1.1 on 2022-10-21 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0016_alter_apartments_price_alter_building_price_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.CharField(max_length=50)),
                ('subject', models.CharField(max_length=50)),
                ('message', models.TextField()),
            ],
        ),
    ]
