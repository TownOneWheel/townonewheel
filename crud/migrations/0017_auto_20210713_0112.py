# Generated by Django 3.2.4 on 2021-07-13 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0016_merge_20210708_0836'),
    ]

    operations = [
        migrations.AddField(
            model_name='cat',
            name='created_at',
            field=models.TextField(default=1626138764.3394933),
        ),
        migrations.AddField(
            model_name='cat',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='cat',
            name='updated_at',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='created_at',
            field=models.TextField(default=1626138764.3394933),
        ),
        migrations.AddField(
            model_name='comment',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='comment',
            name='updated_at',
            field=models.TextField(blank=True, null=True),
        ),
    ]
