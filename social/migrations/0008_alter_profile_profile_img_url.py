from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0007_auto_20210713_0117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_img_url',
            field=models.TextField(blank=True, default=True, null=True),
        ),
    ]
