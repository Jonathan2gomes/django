# Generated by Django 3.2.9 on 2021-12-01 03:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ronda', '0003_auto_20211130_1905'),
    ]

    operations = [
        migrations.CreateModel(
            name='Venda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota_fiscal', models.IntegerField(max_length=9)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ronda.cliente')),
                ('moto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ronda.moto')),
            ],
        ),
    ]
