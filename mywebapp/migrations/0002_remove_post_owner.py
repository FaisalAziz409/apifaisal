# Generated by Django 3.1 on 2020-08-20 15:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mywebapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='owner',
        ),
    ]
