from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from .models import Profile, User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    model = User
    list_display = ['username', 'email',
                    'is_staff', 'is_active', 'upper_get_full_name'
                    ]
    list_filter = ['username', 'email', 'is_staff', 'is_active']
    fieldsets = (
        (_("Авторизация"), {'fields': ('username', 'email', 'password')}),
        (_("Персональная информация"), {
            'fields': (
                'first_name', 'last_name'
            )}),
        (_("Разрешения"), {
            'fields': ('is_staff', 'is_active', 'is_superuser',)}),
        (_("Дополнительная информация"), {
            'fields': ('last_login', 'date_joined',)}),

    )
    add_fieldsets = (
        (None,
         {
             "classes": ("wide",),
             'fields': (
                 'username',
                 'email',
                 'password1',
                 'password2',
                 'is_staff',
                 'is_active'
             )
         }),
    )

    def upper_get_full_name(self, obj):
        return f'{obj.get_full_name()}'

    upper_get_full_name.short_description = 'ФИ'


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['get_user_username', 'get_user_email', 'gender',
                    'date_of_brith', 'get_calories_per_day', 'get_age']

    def get_user_username(self, obj):
        return obj.user.username

    def get_user_email(self, obj):
        return obj.user.email

    def date_of_brith(self, obj):
        return f'{obj.brith_day}.{obj.brith_month}.{obj.brith_year}'

    def str_get_calories_per_day(self, obj):
        return obj.get_calories_per_day()

    def str_get_age(self, obj):
        return obj.get_age()

    str_get_age.short_description = 'Возраст'
    str_get_calories_per_day.short_description = 'Суточная норма калорий'
    get_user_username.short_description = 'Никнейм'
    get_user_email.short_description = 'Электронная почта'
    date_of_brith.short_description = 'Дата рождения'
