# Generated by Django 3.2.4 on 2021-06-06 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neighborhood_app', '0005_alter_neighbourhood_occupants'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='neighbourhood',
            name='admin',
        ),
        migrations.AddField(
            model_name='neighbourhood',
            name='description',
            field=models.TextField(default=''),
        ),
    ]
