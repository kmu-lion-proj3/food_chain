# Generated by Django 2.1.8 on 2019-05-13 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0010_situation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Flag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flag', models.BooleanField()),
            ],
        ),
    ]