# Generated by Django 3.2.4 on 2021-07-15 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0008_alter_profile_profile_img_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_img_url',
            field=models.TextField(blank=True, null=True),
        ),
    ]
