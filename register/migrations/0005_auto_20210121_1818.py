# Generated by Django 3.1.5 on 2021-01-21 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0004_auto_20210121_1816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homeless',
            name='height',
            field=models.DecimalField(decimal_places=1, max_digits=4),
        ),
        migrations.AlterField(
            model_name='homeless',
            name='weight',
            field=models.DecimalField(decimal_places=1, max_digits=4),
        ),
    ]
