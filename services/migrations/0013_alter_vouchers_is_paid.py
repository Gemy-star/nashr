# Generated by Django 4.0.1 on 2022-03-09 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0012_vouchers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vouchers',
            name='is_paid',
            field=models.BooleanField(blank=True, choices=[(True, 'تم الدفع'), (False, 'لم يتم الدفع الدفع')], default=False, null=True),
        ),
    ]
