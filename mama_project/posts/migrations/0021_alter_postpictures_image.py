# Generated by Django 5.1.3 on 2024-12-03 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0020_alter_postpictures_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postpictures',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='image'),
        ),
    ]
