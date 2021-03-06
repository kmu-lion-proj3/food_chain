
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kind', models.CharField(max_length=200)),
                ('status', models.IntegerField()),
                ('victory', models.BooleanField(default=True)),
                ('location', models.CharField(max_length=200)),
                ('limited_location', models.CharField(max_length=200)),
                ('life', models.BooleanField(default=True)),
            ],
        ),
    ]
