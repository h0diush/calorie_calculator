from django.db import models
from django.utils.translation import gettext_lazy as _


class CaloriesModel(models.Model):
    """Модель калорий"""

    user = models.ForeignKey(
        "users.User",
        verbose_name=_("Пользователь"),
        on_delete=models.CASCADE,
        related_name='calories'
    )
    food = models.CharField(
        verbose_name=_("Что я кушал"),
        max_length=255
    )
    qty_calories = models.SmallIntegerField(
        verbose_name=_("Кол-во калорий"),
        default=0,
    )
    created = models.DateTimeField(
        verbose_name=_("Дата"),
        auto_now_add=True
    )

    class Meta:
        verbose_name = 'Калории'
        verbose_name_plural = 'Калории'

    def __str__(self):
        return f'{self.food} - {self.qty_calories}'
