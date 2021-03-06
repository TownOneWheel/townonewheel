# Generated by Django 3.2.4 on 2021-07-04 15:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('social', '0003_alter_profile_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='relationship',
            name='profile',
        ),
        migrations.AddField(
            model_name='relationship',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='relationship', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='relationship',
            name='followers',
            field=models.ManyToManyField(blank=True, related_name='following', to=settings.AUTH_USER_MODEL),
        ),
    ]
