# Generated by Django 2.1.8 on 2019-05-12 07:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0004_auto_20190512_0647'),
    ]

    operations = [
        migrations.RenameField(
            model_name='animal',
            old_name='stare',
            new_name='starve',
        ),
    ]
