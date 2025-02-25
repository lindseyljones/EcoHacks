# Generated by Django 4.2 on 2023-04-15 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vegan', models.BooleanField(default=False)),
                ('vegetarian', models.BooleanField(default=False)),
                ('organic', models.BooleanField(default=False)),
                ('meat_type', models.CharField(choices=[(1, 'pork'), (2, 'poultry'), (3, 'beef'), (4, 'seafood')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='MaterialGoods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(choices=[(1, 'water bottle'), (2, 'reusable bag'), (3, 'technology')], max_length=1)),
                ('months_owned', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Transportation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carpool', models.BooleanField(default=False)),
                ('secondhand', models.BooleanField(default=False)),
                ('type', models.CharField(choices=[(1, 'bus'), (2, 'car'), (3, 'bike'), (4, 'electric scooter/bike'), (5, 'walk')], max_length=1)),
            ],
        ),
    ]
