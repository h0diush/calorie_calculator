from django.urls import path

from .views import (CalorieCounterView, DeleteColorieView,
                    FoodCaloriesCreateView)

urlpatterns = [
    path('', CalorieCounterView.as_view(), name='index'),
    path('<int:pk>/delete/', DeleteColorieView.as_view(),
         name='delete_calories'),
    path('create/', FoodCaloriesCreateView.as_view(),
         name='crete_calories_food'),
]
