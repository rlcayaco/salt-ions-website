# Generated by Django 3.1.4 on 2021-04-19 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0011_auto_20210419_0039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectmainmodel',
            name='project_main_image',
            field=models.ImageField(blank=True, default='placeholder-image.png', null=True, upload_to='project_images/main_images/'),
        ),
    ]