# Generated by Django 3.2.4 on 2021-06-29 05:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=8)),
                ('profile_img_url', models.TextField()),
                ('introduction', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('created_at', models.TextField()),
                ('updated_at', models.TextField()),
                ('is_deleted', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Relationship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('followers', models.ManyToManyField(related_name='relationship', to='social.Profile')),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='myrelationship', to='social.profile')),
            ],
        ),
    ]
