# Generated by Django 4.0.1 on 2022-02-08 18:00

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_publishingbook'),
    ]

    operations = [
        migrations.AddField(
            model_name='publishingbook',
            name='first_rule_ar',
            field=models.CharField(help_text='SubTitle for MemberShipTerms Page [Arabic]', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='publishingbook',
            name='first_rule_en',
            field=models.CharField(help_text='SubTitle for MemberShipTerms Page [English]', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='publishingbook',
            name='general_content_ar',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='publishingbook',
            name='general_content_en',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='publishingbook',
            name='general_roles_ar',
            field=models.CharField(help_text='general terms for MemberShipTerms Page [Arabic]', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='publishingbook',
            name='general_roles_en',
            field=models.CharField(help_text='general terms for MemberShipTerms Page [English]', max_length=255, null=True),
        ),
    ]