# Generated by Django 3.2.5 on 2022-04-26 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Snack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('snack_name', models.CharField(max_length=50)),
                ('snack_brand', models.CharField(max_length=100)),
                ('snack_price', models.IntegerField(default=0)),
                ('snack_producer', models.CharField(max_length=100)),
                ('snack_stock_unit', models.CharField(max_length=10)),
                ('quantity', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
