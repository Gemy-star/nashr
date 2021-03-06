# Generated by Django 4.0.1 on 2022-02-02 21:46

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WhoUS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading_en', models.CharField(help_text='Title for Who Us Page [English]', max_length=255, null=True)),
                ('heading_ar', models.CharField(help_text='Title for Who Us Page [Arabic]', max_length=255, null=True)),
                ('content_en', ckeditor.fields.RichTextField(help_text='Content for Who Us Page [English]')),
                ('content_ar', ckeditor.fields.RichTextField(help_text='Content for Who Us Page [Arabic]')),
            ],
        ),
    ]
