# Generated by Django 3.1.1 on 2020-10-24 05:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0011_remove_orderitem_cust'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='complete',
        ),
    ]