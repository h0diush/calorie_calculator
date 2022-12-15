from django.contrib import messages
from django.contrib.auth import get_user_model, logout, views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import DetailView, FormView, UpdateView
from django.views.generic.base import TemplateView
from registration.backends.default.views import RegistrationView

from .forms import PasswordResetForm, ProfileUserForm, RegisterForm
from .models import Profile

User = get_user_model()


def index(request):
    return render(request, 'index.html')


class RegistrationUserView(RegistrationView):
    """Регистрация пользователей"""

    form_class = RegisterForm
    template_name = 'users/register.html'

    def get_success_url(self, user=None):
        return reverse('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация'
        return context

    def form_valid(self, form):
        messages.add_message(
            self.request, messages.INFO,
            'Электронное письмо для подтверждения аккаунта успешно отправлено'
        )
        return super().form_valid(form)


def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')


class ActivationEmailComplete(TemplateView):
    """Подтверждение электронной почты"""

    template_name = 'registration/activation_completed.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Почта активирована'
        return context


class PasswordResetView(views.PasswordResetView):
    """Проверка перед восстановлением пароля,
       существует есть ли email в бд """

    form_class = PasswordResetForm


class PasswordChange(views.PasswordChangeView):
    """Изменение пароля"""

    title = 'Изменение пароля'


class LoginUserView(LoginView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Вход'
        return context


class UserProfileCreateView(LoginRequiredMixin, FormView):
    """Профиль пользователя"""

    def dispatch(self, request, *args, **kwargs):
        if Profile.objects.filter(user=self.request.user):
            return HttpResponseForbidden()
        return super().dispatch(request, *args, **kwargs)

    template_name = "users/profile_user_create.html"
    form_class = ProfileUserForm
    success_url = '/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)


class UserProfileDetailView(LoginRequiredMixin, DetailView):
    """ Профиль пользователя"""
    # TODO dispatch  404 если пользователь анонимный
    context_object_name = 'user'
    template_name = 'users/user_profile_detail.html'
    model = User
    slug_field = 'username'
    slug_url_kwarg = 'username'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = Profile.objects.filter(user=self.request.user).first()
        if profile:
            context["profile"] = profile
        else:
            context["profile"] = None
        return context


class UpdateUserProfile(LoginRequiredMixin, UpdateView):
    """Обновление профиля пользователя"""

    # def dispatch(self, request, *args, **kwargs):
    #     profile_user = Profile.objects.filter(user=request.user).first()
    #     if request.user != profile_user.user:
    #         return HttpResponseForbidden()
    #     return super().dispatch(request, *args, **kwargs)

    model = Profile
    context_object_name = 'profile'
    form_class = ProfileUserForm
    template_name = 'users/profile_user_update.html'
    pk_url_kwarg = 'pk'
    # slug_field = 'username'
    # slug_url_kwarg = 'username'
    success_url = '/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)
