# Generated by Django 2.1.4 on 2019-02-03 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_cybernatics_protetor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='success_stories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('story_title', models.CharField(max_length=30)),
                ('Description', models.CharField(max_length=100)),
            ],
        ),
    ]
