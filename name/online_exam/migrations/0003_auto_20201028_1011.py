# Generated by Django 2.2 on 2020-10-28 10:11

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('online_exam', '0002_auto_20201028_0958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mcq',
            name='question',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
