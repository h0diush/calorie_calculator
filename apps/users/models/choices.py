import datetime as dt

from django.db import models

CURRENT_YEAR = dt.datetime.now().year


class Gender(models.TextChoices):
    """Пол"""

    MAN = 'MAN', 'Мужчина'
    GIRL = 'GIRL', 'Женщина'


DAYS = [(f'{day}', f'{day}') for day in range(1, 31 + 1)]
MONTHS = [
    ('1', 'Январь'),
    ('2', 'Февраль'),
    ('3', 'Март'),
    ('4', 'Апрель'),
    ('5', 'Май'),
    ('6', 'Июнь'),
    ('7', 'Июль'),
    ('8', 'Август'),
    ('9', 'Сентябрь'),
    ('10', 'Октябрь'),
    ('11', 'Ноябрь'),
    ('12', 'Декабрь'),
]

YEARS = [(f'{year}', f'{year}') for year in
         range(CURRENT_YEAR - 60, CURRENT_YEAR + 1)]


class WorkoutChoice(models.TextChoices):
    """Список тренировок"""

    PASSIVE_LIFESTYLE = 'PASSIVE_LIFESTYLE', 'Сидячий образ жизни без нагрузок'
    WORKOUT_1_3_TIMES_A_WEEK = 'WORKOUT_1_3_TIMES_A_WEEK', 'Тренировки  1-3 раза в неделю'
    CLASSES_3_5_DAYS_A_WEEK = 'CLASSES_3_5_DAYS_A_WEEK', 'Занятия 3-5 дней в неделю'
    INTENSE_WORKOUT = 'INTENSE_WORKOUT', 'Интенсивные тренировки 6-7 раз в неделю'
    ATHLETES = 'ATHLETES', 'Спортсмены, выполняющие упражнения чаще, чем раз в день'
