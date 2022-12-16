from django.views.generic import ListView

from .models import CaloriesModel
# f

class CalorieCounterView(ListView):
    context_object_name = 'calories'
    template_name = 'calories/food_list.html'

    def get_queryset(self):
        if not self.request.user.is_anonymous:
            return CaloriesModel.objects.filter(user=self.request.user)
        return None
