# Generated by Django 2.1.4 on 2019-02-03 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_cybernatics_protetor', '0007_tips'),
    ]

    operations = [
        migrations.CreateModel(
            name='Applicants',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('JOB_TITLE', models.CharField(max_length=30)),
                ('First_Name', models.CharField(max_length=30)),
                ('Last_Name', models.CharField(max_length=30)),
                ('Dob', models.DateField()),
                ('Qualification', models.CharField(max_length=30)),
                ('percentage', models.IntegerField()),
                ('Institute', models.CharField(max_length=30)),
                ('Experience', models.IntegerField()),
                ('Contact_Number', models.IntegerField()),
            ],
        ),
    ]
