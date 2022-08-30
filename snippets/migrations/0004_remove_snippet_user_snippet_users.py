# Generated by Django 4.1 on 2022-08-29 15:20

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0003_language_alter_snippet_language'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='snippet',
            name='user',
        ),
        migrations.AddField(
            model_name='snippet',
            name='users',
            field=models.ManyToManyField(blank=True, related_name='snippets', to=settings.AUTH_USER_MODEL),
        ),
    ]
