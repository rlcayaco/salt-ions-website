# Generated by Django 3.1.4 on 2021-04-19 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_auto_20210419_0028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectmainmodel',
            name='project_main_image',
            field=models.ImageField(blank=True, default='images/placeholder-image.png', null=True, upload_to='project_images/main_images/'),
        ),
    ]
