from django import forms
from django.contrib.auth.forms import PasswordResetForm as ResetForm, \
    UserCreationForm

from .models import Profile, User
from .models.choices import DAYS, Gender, MONTHS, WorkoutChoice, YEARS
from .validators import validate_height_weight


class RegisterForm(UserCreationForm):
    """Форма регистрации пользователя"""

    username = forms.CharField(label='Никнейм', widget=forms.TextInput())
    email = forms.EmailField(
        label='Электронная почта', widget=forms.EmailInput())
    first_name = forms.CharField(label='Имя', widget=forms.TextInput())
    last_name = forms.CharField(label='Фамилия', widget=forms.TextInput())
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput())
    password2 = forms.CharField(
        label='Повторите пароль', widget=forms.PasswordInput())

    class Meta(UserCreationForm.Meta):
        model = User
        fields = (
            'username', 'email', 'first_name', 'last_name',
        )

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                f'Пользователь с {email} уже существует')
        return email

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(
                f'Пользователь с никнеймом {username} уже существует')
        return username

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 != password2:
            raise forms.ValidationError('Пароли не совпадают')
        return password2


class PasswordResetForm(ResetForm):
    """Форма валидации электронной почты,
     существует ли пользователь в бд. Для восстановления пароля"""

    def clean_email(self):
        email = self.cleaned_data['email']
        if not User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                f'Почта {email} не зарегистрирована на сайте')
        return email


class ProfileUserForm(forms.ModelForm):
    """Форма для заполнения профиля пользователя"""

    gender = forms.ChoiceField(
        label='Пол:', widget=forms.Select(),
        choices=Gender.choices
    )
    brith_day = forms.ChoiceField(
        label='День:', widget=forms.Select(),
        choices=[day for day in DAYS]
    )

    brith_month = forms.ChoiceField(
        label='Месяц:', widget=forms.Select(),
        choices=[month for month in MONTHS]
    )

    brith_year = forms.ChoiceField(
        label='Год:', widget=forms.Select(),
        choices=[year for year in YEARS]
    )

    height = forms.CharField(
        label='Рост:', max_length=3, validators=[validate_height_weight],
        help_text="Рост должен быть в см",
        widget=forms.TextInput()
    )

    weight = forms.CharField(
        label='Вес:', max_length=3, validators=[validate_height_weight],
        help_text="Вес должен быть в кг",
        widget=forms.TextInput()
    )

    workout = forms.ChoiceField(
        label='Занятия спортом:', widget=forms.Select(),
        choices=WorkoutChoice.choices
    )

    class Meta:
        model = Profile
        exclude = ('user',)
