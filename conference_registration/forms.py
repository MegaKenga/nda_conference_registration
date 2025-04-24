from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

from conference_registration.models import Person


class AddPartnerToConferenceList(forms.ModelForm):
    last_name = forms.CharField(max_length=50, required=True, label='Ваша фамилия')
    first_name = forms.CharField(max_length=50, required=True, label='Ваше имя')
    father_name = forms.CharField(max_length=50, required=True, label='Ваше отчество')
    company_inn = forms.CharField(max_length=50, required=True, label='ИНН организации')
    person_email = forms.EmailField(label='Email для связи', required=True)
    person_phone = forms.CharField(max_length=50, required=True, label='Контактный телефон')
    company_related_manager = forms.ChoiceField(choices=Person.MANAGER, required=True, label='Ваш менеджер в НДА Деловая медицинская компания')

    class Meta:
        model = Person
        fields = '__all__'


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ['username', 'password']