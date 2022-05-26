# Generated by Django 3.2.9 on 2022-05-16 14:55

import datetime
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('message', models.CharField(max_length=2000)),
                ('created_at', models.TimeField(blank=True, default=datetime.datetime.now)),
                ('updated_at', models.TimeField(blank=True, default=datetime.datetime.now)),
                ('dom_element', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
