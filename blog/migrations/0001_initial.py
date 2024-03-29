# Generated by Django 4.2 on 2023-04-08 16:27

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=10)),
                ('publish', models.DateTimeField(default=datetime.datetime(2023, 4, 8, 16, 27, 23, 657841, tzinfo=datetime.timezone.utc))),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posted', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
