# Generated by Django 3.2 on 2021-07-18 12:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_liked'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='like',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.PROTECT, to='blog.liked'),
        ),
    ]