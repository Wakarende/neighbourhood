# Generated by Django 3.2.4 on 2021-06-05 17:14

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('neighborhood_app', '0003_neighbourhood_occupants'),
        ('user', '0002_usermodel_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='Profile Picture')),
                ('bio', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('neighbourhood', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='occupants_count', to='neighborhood_app.neighbourhood')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='UserModel',
        ),
    ]