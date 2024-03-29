# Generated by Django 2.2.6 on 2019-10-06 12:54

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0005_auto_20191006_1208'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', ckeditor.fields.RichTextField()),
            ],
            options={
                'verbose_name': 'cms',
                'verbose_name_plural': 'cms',
                'db_table': 'cms',
            },
        ),
    ]
