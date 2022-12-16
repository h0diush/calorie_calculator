from django.urls import path

from .views import CalorieCounterView

urlpatterns = [
    path('', CalorieCounterView.as_view(), name='index')
]
