# Generated by Django 4.1.5 on 2023-01-26 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_news_options_alter_news_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='link',
            field=models.URLField(blank=True, null=True),
        ),
    ]