# Generated by Django 3.2 on 2021-07-18 17:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_rename_like_post_archive'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='archive',
            new_name='like',
        ),
    ]
