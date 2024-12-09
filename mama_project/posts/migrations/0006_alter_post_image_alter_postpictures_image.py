# Generated by Django 5.1.3 on 2024-11-16 08:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_post_postcountry_postpictures_delete_postmodel_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.FileField(upload_to='image/'),
        ),
        migrations.AlterField(
            model_name='postpictures',
            name='image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.post'),
        ),
    ]
