# Generated by Django 4.0 on 2022-05-04 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storeapp', '0009_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.IntegerField(max_length=250),
        ),
    ]