# Generated by Django 5.0.1 on 2024-02-16 12:22

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('duolar', '0002_alter_umraduo_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='umraduo',
            name='description_ky',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='umraduo',
            name='description_uz',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='umraduo',
            name='name_ky',
            field=models.CharField(max_length=331, null=True),
        ),
        migrations.AddField(
            model_name='umraduo',
            name='name_uz',
            field=models.CharField(max_length=331, null=True),
        ),
    ]
