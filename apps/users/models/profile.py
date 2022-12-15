from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.users.models.choices import DAYS, Gender, MONTHS, WorkoutChoice, \
    YEARS
from apps.users.utils import calorie_calculation, get_persons_age
from apps.users.validators import validate_height_weight


class Profile(models.Model):
    """Модель профиля пользователя"""

    user = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        verbose_name=_("Пользователь"),
        related_name='profiles'
    )
    gender = models.CharField(
        max_length=15, verbose_name=_("Пол"),
        choices=Gender.choices, default=Gender.MAN
    )
    brith_day = models.CharField(
        max_length=2, verbose_name=_("День"),
        choices=DAYS
    )
    brith_month = models.CharField(
        max_length=2, verbose_name=_("Месяц"),
        choices=MONTHS
    )
    brith_year = models.CharField(
        max_length=4, verbose_name=_("Год"),
        choices=YEARS
    )

    height = models.CharField(
        _("Рост"), max_length=3,
        validators=[validate_height_weight],
        help_text="Необходимо указывать в см"
    )

    weight = models.CharField(
        _("Вес"), max_length=3,
        validators=[validate_height_weight],
        help_text="Необходимо указывать в кг"
    )

    workout = models.CharField(
        max_length=55, verbose_name=_("Пол"),
        choices=WorkoutChoice.choices,
        default=WorkoutChoice.PASSIVE_LIFESTYLE
    )

    @property
    def get_age(self):
        """Возвращает возраст пользователя"""

        return get_persons_age(
            int(self.brith_day),
            int(self.brith_month),
            int(self.brith_year)
        )

    @property
    def get_calories_per_day(self):
        """Возвращает суточная норма калорий"""
        return calorie_calculation(
            self.gender, int(self.weight),
            int(self.height), self.get_age,
            self.workout
        )

    class Meta:
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профили пользователей'

    def __str__(self):
        return self.user.username
