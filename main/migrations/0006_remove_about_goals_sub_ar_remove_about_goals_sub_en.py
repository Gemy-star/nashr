# Generated by Django 4.0.1 on 2022-02-05 13:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_homepage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='about',
            name='goals_sub_ar',
        ),
        migrations.RemoveField(
            model_name='about',
            name='goals_sub_en',
        ),
    ]
