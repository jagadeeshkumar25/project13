# Generated by Django 2.0 on 2021-09-16 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Manager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addingdetails',
            name='LAST_DAY_TO_APPLY',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='addingdetails',
            name='RESISTARTION_START_FORM',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
