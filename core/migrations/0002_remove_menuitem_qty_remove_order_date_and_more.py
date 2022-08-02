# Generated by Django 4.0.6 on 2022-08-01 21:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menuitem',
            name='qty',
        ),
        migrations.RemoveField(
            model_name='order',
            name='date',
        ),
        migrations.RemoveField(
            model_name='order',
            name='menu_items',
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='image',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='order',
            name='courier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.courier'),
        ),
        migrations.AlterField(
            model_name='order',
            name='tax',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='order',
            name='tip',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='order',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField(default=1)),
                ('menu_items', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.menuitem')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.order')),
            ],
        ),
    ]