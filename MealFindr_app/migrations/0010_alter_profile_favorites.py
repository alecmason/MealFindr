# Generated by Django 3.2.9 on 2022-02-02 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MealFindr_app', '0009_profile_favorites'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='favorites',
            field=models.ManyToManyField(blank=True, to='MealFindr_app.Eatery'),
        ),
    ]
