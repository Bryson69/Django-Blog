# Generated by Django 3.2 on 2021-07-18 18:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20210718_2141'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='archive',
            new_name='like',
        ),
    ]
