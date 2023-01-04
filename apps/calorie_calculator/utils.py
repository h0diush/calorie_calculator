from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse_lazy

from apps.users.models import Profile

User = get_user_model()


def calculation_of_remaining_calories(username, calories_burned,
                                      method):
    """Расчет оставшихся калорий"""

    user = User.objects.get(username=username)
    try:
        profile_user = Profile.objects.get(user=user)
    except ObjectDoesNotExist:
        return reverse_lazy('create_profile')

    if method == 'create':
        user.calories_burned += calories_burned
    elif method == 'delete':
        user.calories_burned -= calories_burned
    user.remaining_calories = int(
        profile_user.get_calories_per_day) - user.calories_burned
    user.save()
