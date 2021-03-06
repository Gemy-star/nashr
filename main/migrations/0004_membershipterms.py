# Generated by Django 4.0.1 on 2022-02-03 15:47

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_about'),
    ]

    operations = [
        migrations.CreateModel(
            name='MembershipTerms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading_en', models.CharField(help_text='Title for MemberShipTerms Page [English]', max_length=255, null=True)),
                ('heading_ar', models.CharField(help_text='Title for MemberShipTerms Page [Arabic]', max_length=255, null=True)),
                ('sub_heading_en', models.CharField(help_text='SubTitle for MemberShipTerms Page [English]', max_length=255, null=True)),
                ('sub_heading_ar', models.CharField(help_text='SubTitle for MemberShipTerms Page [Arabic]', max_length=255, null=True)),
                ('section_one_en', ckeditor.fields.RichTextField(help_text='Section one for MemberShipTerms Page [English]', null=True)),
                ('section_one_ar', ckeditor.fields.RichTextField(help_text='Section one for MemberShipTerms Page [Arabic]', null=True)),
                ('section_two_en', ckeditor.fields.RichTextField(help_text='Section two for MemberShipTerms Page [English]', null=True)),
                ('section_two_ar', ckeditor.fields.RichTextField(help_text='Section two for MemberShipTerms Page [Arabic]', null=True)),
                ('section_three_en', ckeditor.fields.RichTextField(help_text='Section three for MemberShipTerms Page [English]', null=True)),
                ('section_three_ar', ckeditor.fields.RichTextField(help_text='Section three for MemberShipTerms Page [Arabic]', null=True)),
                ('section_four_en', ckeditor.fields.RichTextField(help_text='Section four for MemberShipTerms Page [English]', null=True)),
                ('section_four_ar', ckeditor.fields.RichTextField(help_text='Section four for MemberShipTerms Page [Arabic]', null=True)),
                ('section_five_en', ckeditor.fields.RichTextField(help_text='Section five for MemberShipTerms Page [English]', null=True)),
                ('section_five_ar', ckeditor.fields.RichTextField(help_text='Section five for MemberShipTerms Page [Arabic]', null=True)),
                ('section_six_en', ckeditor.fields.RichTextField(help_text='Section six for MemberShipTerms Page [English]', null=True)),
                ('section_six_ar', ckeditor.fields.RichTextField(help_text='Section six for MemberShipTerms Page [Arabic]', null=True)),
                ('section_seven_en', ckeditor.fields.RichTextField(help_text='Section seven for MemberShipTerms Page [English]', null=True)),
                ('section_seven_ar', ckeditor.fields.RichTextField(help_text='Section seven for MemberShipTerms Page [Arabic]', null=True)),
            ],
        ),
    ]
