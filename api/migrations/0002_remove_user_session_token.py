# Generated by Django 3.0.8 on 2020-07-31 04:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='session_token',
        ),
    ]
