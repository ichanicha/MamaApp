# Generated by Django 5.1.3 on 2024-11-14 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_alter_postmodel_address_alter_postmodel_free_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
    ]
