# Generated by Django 3.1.5 on 2021-01-22 16:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_addiction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homeless',
            name='cpf',
            field=models.CharField(blank=True, max_length=14, unique=True, verbose_name='CPF'),
        ),
        migrations.AlterField(
            model_name='homeless',
            name='rg',
            field=models.CharField(blank=True, max_length=13, unique=True, verbose_name='RG'),
        ),
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_disease', models.CharField(max_length=90)),
                ('type_disease', models.CharField(max_length=90)),
                ('homeless', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='register.homeless')),
            ],
            options={
                'db_table': 'Disease',
            },
        ),
    ]
