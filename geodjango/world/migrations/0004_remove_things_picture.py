# Generated by Django 3.2.7 on 2021-09-28 04:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('world', '0003_auto_20210927_0200'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='things',
            name='picture',
        ),
    ]