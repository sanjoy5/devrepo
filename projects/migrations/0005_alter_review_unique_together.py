# Generated by Django 4.2.3 on 2023-08-10 16:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_skill'),
        ('projects', '0004_project_owner_review_owner'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='review',
            unique_together={('owner', 'project')},
        ),
    ]