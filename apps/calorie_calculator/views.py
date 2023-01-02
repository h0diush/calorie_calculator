from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.urls import reverse_lazy
from django.views.generic import DeleteView, FormView, ListView, UpdateView

from .forms import CalorieCounterFormCreate
from .models import CaloriesModel
from .utils import calculation_of_remaining_calories
from ..users.models import Profile


class CalorieCounterView(ListView):
    """Вывод потраченных калорий"""

    context_object_name = 'calories'
    template_name = 'calories/food_list.html'

    def get_queryset(self):
        if not self.request.user.is_anonymous:
            return CaloriesModel.objects.filter(user=self.request.user)
        return None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if not self.request.user.is_anonymous:
            context["profile"] = Profile.objects.get(user=self.request.user)
        return context


class DeleteColorieView(DeleteView):
    """Удаление потраченных калорий"""

    model = CaloriesModel
    success_url = reverse_lazy('index')

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def form_valid(self, form):
        calculation_of_remaining_calories(
            self.request.user.username,
            self.get_object().qty_calories,
            'delete'
        )
        return super().form_valid(form)

    def get_object(self, queryset=None):
        obj = super(DeleteColorieView, self).get_object()
        if not obj.user == self.request.user:
            raise Http404
        return obj


class FoodCaloriesCreateView(LoginRequiredMixin, FormView):
    """Создание потраченных калорий"""
    form_class = CalorieCounterFormCreate
    template_name = 'calories/create_calories_food.html'
    success_url = '/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        calculation_of_remaining_calories(
            self.request.user.username,
            form.instance.qty_calories,
            'create'
        )
        form.save()
        return super().form_valid(form)


class FoodCaloriesUpdateView(UpdateView):
    """Изменение потраченных калорий"""

    pass
