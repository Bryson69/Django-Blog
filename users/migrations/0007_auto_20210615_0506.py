# Generated by Django 3.2 on 2021-06-15 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20210615_0424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='facebook_social',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='github_social',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='linkedIn_social',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='twitter_social',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
