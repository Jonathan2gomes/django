# Generated by Django 3.2.9 on 2021-11-30 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ronda', '0002_moto_ano'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='moto',
            name='nivel',
        ),
        migrations.AddField(
            model_name='moto',
            name='marca',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='moto',
            name='ano',
            field=models.CharField(default='2020', max_length=10),
        ),
        migrations.AlterField(
            model_name='moto',
            name='descricao',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='moto',
            name='preco',
            field=models.FloatField(max_length=10),
        ),
    ]
