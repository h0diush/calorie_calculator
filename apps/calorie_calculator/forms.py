from django import forms

from .models import CaloriesModel


<<<<<<< HEAD
class CalorieCounterFormCreate(forms.ModelForm):
=======
class CalorieCounterForm(forms.ModelForm):
>>>>>>> origin/main
    """Форма заполнения полученных калорий"""

    class Meta:
        model = CaloriesModel
        exclude = ('user',)
