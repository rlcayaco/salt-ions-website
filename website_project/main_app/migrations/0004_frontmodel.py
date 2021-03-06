# Generated by Django 3.1.4 on 2021-04-08 00:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_carouselmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='FrontModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('front_name', models.CharField(max_length=60)),
                ('front_image', models.ImageField(upload_to='project_images/front_images/')),
                ('project_main', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='front', to='main_app.projectmainmodel')),
            ],
        ),
    ]
