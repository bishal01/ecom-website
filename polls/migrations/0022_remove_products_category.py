# Generated by Django 3.1.1 on 2020-10-29 04:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0021_auto_20201029_0953'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='category',
        ),
    ]
