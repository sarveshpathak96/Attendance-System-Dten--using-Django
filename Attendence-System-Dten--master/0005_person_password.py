# Generated by Django 2.1.3 on 2018-12-19 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dtenapp', '0004_subject_creator'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='password',
            field=models.CharField(default='SOME STRING', max_length=100),
        ),
    ]