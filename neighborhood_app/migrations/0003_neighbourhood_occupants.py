# Generated by Django 3.2.4 on 2021-06-05 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neighborhood_app', '0002_remove_neighbourhood_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='neighbourhood',
            name='occupants',
            field=models.IntegerField(default=0),
        ),
    ]
