# Generated by Django 2.1.4 on 2019-02-03 04:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_cybernatics_protetor', '0003_job_postings'),
    ]

    operations = [
        migrations.DeleteModel(
            name='adminlogin',
        ),
        migrations.DeleteModel(
            name='success_stories',
        ),
        migrations.RemoveField(
            model_name='job_postings',
            name='Experience',
        ),
        migrations.RemoveField(
            model_name='job_postings',
            name='Job',
        ),
        migrations.RemoveField(
            model_name='job_postings',
            name='Last_date',
        ),
        migrations.RemoveField(
            model_name='job_postings',
            name='Location',
        ),
        migrations.RemoveField(
            model_name='job_postings',
            name='Percentage',
        ),
        migrations.RemoveField(
            model_name='job_postings',
            name='Qualification',
        ),
        migrations.RemoveField(
            model_name='job_postings',
            name='Salary',
        ),
    ]