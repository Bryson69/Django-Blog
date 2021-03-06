# Generated by Django 3.2 on 2021-07-18 12:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_rename_content_comment_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='date_posted',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='category',
            name='text',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
