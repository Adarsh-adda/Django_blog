# Generated by Django 3.2.9 on 2021-12-10 11:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_post_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='slug',
        ),
    ]
