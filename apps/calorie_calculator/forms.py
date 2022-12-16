from django import forms

from .models import CaloriesModel


class CalorieCounterFormCreate(forms.ModelForm):
    """Форма заполнения полученных калорий"""

    class Meta:
        model = CaloriesModel
        exclude = ('user',)
