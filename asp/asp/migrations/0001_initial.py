# Generated by Django 2.1.2 on 2018-10-30 09:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Distance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distance', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('latitude', models.FloatField()),
                ('longtitude', models.FloatField()),
                ('altitude', models.FloatField()),
                ('role', models.CharField(choices=[('SP', 'Supplying Hospital'), ('DM', 'Demanding Hospital')], default='DM', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('supplying_hospital', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('weight', models.PositiveIntegerField(default=0)),
                ('quantity', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('QFP', 'Queued for Processing'), ('PBW', 'Processing by Warehouse'), ('QFD', 'Queued for Dispatched'), ('DSD', 'Dispatched'), ('DLD', 'Delivered')], default='QFP', max_length=3)),
                ('time', models.DateTimeField()),
                ('priority', models.PositiveIntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Ordered_Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=200)),
                ('quantity', models.PositiveIntegerField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asp.Order')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('hospital', models.CharField(max_length=50)),
                ('role', models.CharField(choices=[('CM', 'Clinic Manager'), ('DP', 'Dispatcher'), ('WP', 'Warehouse Personnel'), ('AD', 'Admin')], default='CM', max_length=2)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='requester',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asp.User'),
        ),
        migrations.AddField(
            model_name='distance',
            name='from_host',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_host', to='asp.Hospital'),
        ),
        migrations.AddField(
            model_name='distance',
            name='to_host',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_host', to='asp.Hospital'),
        ),
    ]