# Generated by Django 4.0 on 2021-12-26 17:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='owner',
        ),
    ]