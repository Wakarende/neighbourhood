# Generated by Django 3.2.4 on 2021-06-04 10:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('neighborhood_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='neighbourhood',
            name='count',
        ),
    ]
