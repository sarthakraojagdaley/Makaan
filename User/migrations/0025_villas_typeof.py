# Generated by Django 4.1.1 on 2022-10-21 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0024_villas_bhk'),
    ]

    operations = [
        migrations.AddField(
            model_name='villas',
            name='typeof',
            field=models.CharField(default='sell', max_length=50),
        ),
    ]
