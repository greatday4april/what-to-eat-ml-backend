# Generated by Django 3.0.8 on 2020-07-31 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_user_session_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='session_key',
            field=models.CharField(max_length=240, null=True),
        ),
    ]
