# Generated by Django 3.2.6 on 2021-10-01 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('world', '0006_panoimg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='panoimg',
            name='picture',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
