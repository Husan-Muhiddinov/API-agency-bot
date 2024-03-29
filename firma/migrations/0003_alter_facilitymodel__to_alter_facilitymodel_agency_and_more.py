# Generated by Django 5.0.1 on 2024-03-04 18:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firma', '0002_agencymodel_alter_facilitymodel_agency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facilitymodel',
            name='_to',
            field=models.DateField(max_length=100, verbose_name='Tugash sanasi '),
        ),
        migrations.AlterField(
            model_name='facilitymodel',
            name='agency',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firma.agencymodel', verbose_name='Firma nomi'),
        ),
        migrations.AlterField(
            model_name='facilitymodel',
            name='contact',
            field=models.IntegerField(verbose_name='Telefon raqami '),
        ),
        migrations.AlterField(
            model_name='facilitymodel',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=11, verbose_name='Narxi'),
        ),
    ]
