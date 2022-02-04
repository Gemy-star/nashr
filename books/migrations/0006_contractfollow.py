# Generated by Django 4.0.1 on 2022-02-02 20:18

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_bookcontract_is_entered_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContractFollow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField(db_index=True, editable=False, verbose_name='order')),
                ('date_added', models.DateField(null=True)),
                ('follow', models.CharField(max_length=200, null=True)),
                ('notes', ckeditor.fields.RichTextField(null=True)),
                ('contract', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.bookcontract')),
            ],
        ),
    ]