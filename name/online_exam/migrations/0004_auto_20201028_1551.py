# Generated by Django 2.2 on 2020-10-28 15:51

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('online_exam', '0003_auto_20201028_1011'),
    ]

    operations = [
        migrations.AddField(
            model_name='mcq',
            name='option_1',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='mcq',
            name='option_2',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='mcq',
            name='option_3',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='mcq',
            name='option_4',
            field=ckeditor.fields.RichTextField(null=True),
        ),
    ]