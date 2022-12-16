from django import forms

from .models import CaloriesModel


class CalorieCounterForm(forms.ModelForm):
    """Форма заполнения полученных калорий"""

    class Meta:
        model = CaloriesModel
        exclude = ('user',)
