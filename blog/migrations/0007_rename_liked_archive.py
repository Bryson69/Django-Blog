# Generated by Django 3.2 on 2021-07-18 12:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_post_like'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Liked',
            new_name='Archive',
        ),
    ]