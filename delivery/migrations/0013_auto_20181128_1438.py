# Generated by Django 2.1.3 on 2018-11-28 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0012_auto_20181124_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deliverytask',
            name='is_declined_by',
            field=models.CharField(default='-1', max_length=200),
        ),
        migrations.AlterField(
            model_name='deliverytask',
            name='priority',
            field=models.CharField(default='low', max_length=6),
        ),
        migrations.AlterField(
            model_name='deliverytask',
            name='status',
            field=models.CharField(default='new', max_length=9),
        ),
    ]