from django import forms

from conference_registration.models import Person


class AddPartnerToConferenceList(forms.ModelForm):
    last_name = forms.CharField(max_length=50, required=True, label='Ваша фамилия')
    first_name = forms.CharField(max_length=50, required=True, label='Ваше имя')
    father_name = forms.CharField(max_length=50, required=True, label='Ваше отчество')
    company_inn = forms.CharField(max_length=50, required=True, label='ИНН организации')
    person_email = forms.EmailField(label='Email для связи', required=True)
    person_phone = forms.CharField(max_length=50, required=True, label='Контактный телефон')
    company_related_manager = forms.ChoiceField(choices=Person.Manager.choices, required=True)

    class Meta:
        model = Person
        fields = '__all__'
