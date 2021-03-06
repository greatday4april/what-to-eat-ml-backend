# Generated by Django 3.0.8 on 2020-08-17 00:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preference',
            name='restaurant_id',
            field=models.CharField(default=None, max_length=120),
        ),
        migrations.AlterField(
            model_name='preference',
            name='type',
            field=models.CharField(choices=[('LIKE', 'Like'), ('DISLIKE', 'Dislike'), ('NEUTRAL', 'Neutral'), ('FAVORITE', 'Favorite')], default=None, max_length=60),
        ),
        migrations.AlterField(
            model_name='preference',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
