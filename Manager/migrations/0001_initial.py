# Generated by Django 2.0 on 2021-09-16 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddingDetails',
            fields=[
                ('OPPERTUNITY_CODE', models.IntegerField(primary_key=True, serialize=False)),
                ('QUALIFICATION', models.CharField(max_length=50)),
                ('RESISTARTION_START_FORM', models.DateTimeField()),
                ('AGE_LIMIT', models.IntegerField()),
                ('LAST_DAY_TO_APPLY', models.DateTimeField()),
                ('DEPARTMENT_ID', models.CharField(max_length=50)),
                ('NO_OF_POSITION', models.IntegerField()),
                ('DESCRIPTION', models.CharField(max_length=50)),
                ('RESPONSIBILITIES', models.CharField(max_length=50)),
                ('CONTACTNO', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ManagerModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('USERNAME', models.CharField(max_length=30)),
                ('PASSWORD', models.CharField(max_length=30)),
            ],
        ),
    ]