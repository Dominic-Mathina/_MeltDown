# Generated by Django 2.1.2 on 2018-12-11 08:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('songr', '0009_auto_20181206_1807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playlistupload',
            name='dejay',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='playlist', to=settings.AUTH_USER_MODEL),
        ),
    ]
