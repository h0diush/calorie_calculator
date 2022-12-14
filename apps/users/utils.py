import datetime as dt


def get_persons_age(day, month, year) -> int:
    """Утилита, которая считает возраст пользователя"""

    current_year = dt.datetime.now().year
    current_month = dt.datetime.now().month
    current_day = dt.datetime.now().day
    user_age = current_year - year
    if month > current_month:
        return user_age - 1
    elif month == current_month:
        if day > current_day:
            return user_age - 1
        return user_age
    return user_age


def calorie_calculation(gender, weight, height, age, workout):
    """Утилита, которая считает суточную норму калорий"""

    if gender == 'MAN':
        bmr = 88.36 + (13.4 * weight) + (4.8 * height) - (5.7 * age)
    else:
        bmr = 447.6 + (9.2 * weight) + (3.1 * height) - (4.3 * age)
    if workout == 'PASSIVE_LIFESTYLE':
        bmr *= 1.2
    if workout == 'WORKOUT_1_3_TIMES_A_WEEK':
        bmr *= 1.375
    if workout == 'CLASSES_3_5_DAYS_A_WEEK':
        bmr *= 1.55
    if workout == 'INTENSE_WORKOUT':
        bmr *= 1.725
    if workout == 'ATHLETES':
        bmr *= 1.9
    return f'{round(bmr, 2)}'
