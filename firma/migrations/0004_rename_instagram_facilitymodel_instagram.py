# Generated by Django 5.0.3 on 2024-03-05 04:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firma', '0003_alter_facilitymodel__to_alter_facilitymodel_agency_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='facilitymodel',
            old_name='Instagram',
            new_name='instagram',
        ),
    ]
