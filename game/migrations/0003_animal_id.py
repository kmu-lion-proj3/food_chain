# Generated by Django 2.1.8 on 2019-05-12 05:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('game', '0002_auto_20190511_0714'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='ID',
            field=models.OneToOneField(default=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]