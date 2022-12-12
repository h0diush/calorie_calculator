from django.db import models
from django.utils.translation import gettext_lazy as _


class CaloriesModel(models.Model):
    """Модель калорий"""

    user = models.ForeignKey(
        "users.User",
        verbose_name=_("Пользователь"),
        on_delete=models.CASCADE

    )
