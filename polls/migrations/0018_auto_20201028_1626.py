# Generated by Django 3.1.1 on 2020-10-28 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0017_products_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='quantity',
            field=models.IntegerField(blank=True, default=6, null=True),
        ),
    ]
