# Generated by Django 3.2 on 2021-07-19 13:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20210719_0823'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Club',
            new_name='Archive',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='club',
            new_name='archive',
        ),
    ]