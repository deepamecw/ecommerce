# Generated by Django 4.0 on 2022-05-04 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storeapp', '0010_alter_order_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.CharField(max_length=250),
        ),
    ]