# Generated by Django 3.1.7 on 2021-06-03 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0002_timestamps_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='intelrequirementform',
            name='intelligence_type_code',
            field=models.CharField(choices=[('Tactical', '1'), ('Military', '2')], max_length=64),
        ),
    ]