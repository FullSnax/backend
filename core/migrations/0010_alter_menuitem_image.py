# Generated by Django 4.0.6 on 2022-07-26 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_rename_car_courier_vehicle_alter_courier_firstname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
