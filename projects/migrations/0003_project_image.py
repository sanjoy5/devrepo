# Generated by Django 4.2.3 on 2023-07-31 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20230729_1844'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='image',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='project_imgs/'),
        ),
    ]
