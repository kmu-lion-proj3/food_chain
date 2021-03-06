# Generated by Django 2.1.8 on 2019-05-12 16:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('game', '0009_auto_20190512_2031'),
    ]

    operations = [
        migrations.CreateModel(
            name='Situation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=200)),
                ('round', models.IntegerField()),
                ('attacked', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attacked', to=settings.AUTH_USER_MODEL)),
                ('attacker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attacker', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
