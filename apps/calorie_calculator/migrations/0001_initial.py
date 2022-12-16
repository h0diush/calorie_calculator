# Generated by Django 4.1.4 on 2022-12-16 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CaloriesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food', models.CharField(max_length=255, verbose_name='Что я кушал')),
                ('qty_calories', models.SmallIntegerField(default=0, verbose_name='Кол-во калорий')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата')),
            ],
            options={
                'verbose_name': 'Калории',
                'verbose_name_plural': 'Калории',
            },
        ),
    ]
