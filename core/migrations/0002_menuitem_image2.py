# Generated by Django 4.0.6 on 2022-08-01 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='image2',
            field=models.CharField(default='', max_length=100),
        ),
    ]
