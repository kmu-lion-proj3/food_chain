# Generated by Django 2.1.8 on 2019-05-12 11:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0006_auto_20190512_1110'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='animal',
            name='ID',
        ),
    ]
