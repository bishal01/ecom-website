# Generated by Django 3.1.1 on 2020-10-27 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0014_auto_20201024_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.CharField(max_length=200, null=True),
        ),
    ]