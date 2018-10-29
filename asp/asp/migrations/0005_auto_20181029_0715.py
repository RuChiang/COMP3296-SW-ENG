# Generated by Django 2.1.2 on 2018-10-29 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asp', '0004_item_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='quantity',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='item',
            name='weight',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
