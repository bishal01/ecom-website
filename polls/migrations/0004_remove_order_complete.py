# Generated by Django 3.1.1 on 2020-10-03 06:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_orderitem_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='complete',
        ),
    ]