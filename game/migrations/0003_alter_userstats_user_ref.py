# Generated by Django 4.2.2 on 2023-07-10 20:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_userstats_fivemin_best_userstats_halfmin_best_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userstats',
            name='user_ref',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='stats', to=settings.AUTH_USER_MODEL),
        ),
    ]
