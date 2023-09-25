# Generated by Django 4.1.7 on 2023-09-14 18:06

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0003_blogcomment_blogpost_remove_post_author_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogcomment',
            name='author',
        ),
        migrations.AlterField(
            model_name='blogcomment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 14, 18, 6, 3, 550525, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 14, 18, 6, 3, 550525, tzinfo=datetime.timezone.utc)),
        ),
    ]
