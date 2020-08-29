# Generated by Django 2.1.4 on 2019-02-03 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_cybernatics_protetor', '0005_delete_job_postings'),
    ]

    operations = [
        migrations.CreateModel(
            name='adminlogin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='CreateAgent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Agent_Name', models.CharField(max_length=30)),
                ('Password', models.CharField(max_length=50)),
                ('Dob', models.DateField()),
                ('Contact_Number', models.IntegerField()),
                ('Qualification', models.CharField(max_length=30)),
                ('Address', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Job_Postings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Job', models.CharField(default=False, max_length=30)),
                ('Title', models.CharField(max_length=30)),
                ('Qualification', models.CharField(max_length=50)),
                ('Percentage', models.IntegerField()),
                ('Experience', models.IntegerField(help_text='In Years')),
                ('Last_date', models.DateField()),
                ('Location', models.CharField(max_length=100)),
                ('Salary', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='success_stories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('story_title', models.CharField(max_length=30)),
                ('Description', models.CharField(max_length=100)),
            ],
        ),
    ]
