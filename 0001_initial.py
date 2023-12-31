# Generated by Django 4.2.1 on 2023-05-18 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='billing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_method', models.TextField(max_length=50)),
                ('payment_amount', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='bus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('find_bus', models.TextField(max_length=50)),
                ('customer_type', models.TextField(max_length=50)),
                ('date_of_travel', models.TextField(max_length=50)),
                ('number_of_seats', models.IntegerField(default=0)),
                ('fare_per_seat', models.IntegerField(default=0)),
                ('total_cost', models.TextField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Tripform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('route', models.TextField(max_length=50)),
                ('duration', models.TextField(max_length=50)),
                ('distance', models.TextField(max_length=50)),
                ('price', models.TextField(max_length=50)),
            ],
        ),
    ]
