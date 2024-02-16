# Generated by Django 5.0.1 on 2024-02-16 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('preperation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='preparation',
            name='name_ky',
            field=models.CharField(max_length=221, null=True),
        ),
        migrations.AddField(
            model_name='preparation',
            name='name_uz',
            field=models.CharField(max_length=221, null=True),
        ),
        migrations.AddField(
            model_name='preparation',
            name='text_ky',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='preparation',
            name='text_uz',
            field=models.TextField(null=True),
        ),
    ]
