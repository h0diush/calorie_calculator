# Generated by Django 4.1.4 on 2023-01-02 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_calories_burned_alter_profile_brith_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='remaining_calories',
            field=models.SmallIntegerField(default=0, verbose_name='Остаточные калории'),
        ),
    ]