# Generated by Django 4.0.1 on 2022-02-07 16:40

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_remove_homepage_address_ar_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='first_section_Service_title_en',
            field=models.CharField(blank=True, help_text='title For Service for Home Page [Arabic]', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='first_sub_heading_en',
            field=ckeditor.fields.RichTextField(help_text='sub Heading for service section [Arabic]', null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='fourth_section_Service_title_en',
            field=models.CharField(blank=True, help_text='title For Service for Home Page [Arabic]', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='fourth_sub_heading_en',
            field=ckeditor.fields.RichTextField(help_text='sub Heading for service section [Arabic]', null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='second_section_Service_title_en',
            field=models.CharField(blank=True, help_text='title For Service for Home Page [Arabic]', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='second_sub_heading_en',
            field=ckeditor.fields.RichTextField(help_text='sub Heading for service section [Arabic]', null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='third_section_Service_title_en',
            field=models.CharField(blank=True, help_text='title For Service for Home Page [Arabic]', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='third_sub_heading_en',
            field=ckeditor.fields.RichTextField(help_text='sub Heading for service section [Arabic]', null=True),
        ),
    ]
