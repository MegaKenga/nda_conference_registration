from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from dotenv import load_dotenv
from dadata import Dadata
import os
import uuid

from conference_registration.models import Person
from conference_registration.forms import AddPartnerToConferenceList, LoginUserForm
from conference_registration.email_sender import EmailSender


load_dotenv()


def get_company_by_inn(company_inn):
    inn = company_inn
    token = os.getenv('TOKEN')
    dadata = Dadata(token)
    result = dadata.find_by_id(name="party", query=str(inn))

    for name in result:
        return name['value']


def get_person_unique_key():
    unique_key = uuid.uuid4().hex
    return unique_key


def index(request):
    return render(request, 'index.html')


def person_add(request):
    if request.method == 'POST':
        form = AddPartnerToConferenceList(request.POST)
        if form.is_valid():
            calculated_company_name = get_company_by_inn(form.cleaned_data['company_inn'])
            generated_person_unique_key = get_person_unique_key()
            try:
                EmailSender.send_messages(request, calculated_company_name, generated_person_unique_key)
                Person.objects.create(
                    last_name=form.cleaned_data['last_name'],
                    first_name=form.cleaned_data['first_name'],
                    father_name=form.cleaned_data['father_name'],
                    company_inn=form.cleaned_data['company_inn'],
                    company_name=calculated_company_name,
                    person_email=form.cleaned_data['person_email'],
                    person_phone=form.cleaned_data['person_phone'],
                    company_related_manager=form.cleaned_data['company_related_manager'],
                    person_unique_key=str(generated_person_unique_key)
                )
            except Exception as e:
                print(f'email_send failed due to: {e}')
                response = HttpResponse(status=500)
                return response
            return redirect('confirmation')
        else:
            print(form.errors)
    else:
        form = AddPartnerToConferenceList()
    return render(request, 'addperson.html', {'form': form})


def confirmation(request):
    return render(request, 'confirmation.html')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'login.html'
    extra_context = {'title': "Авторизация"}

    def get_success_url(self):
        return reverse_lazy('list_registered')


@login_required
def list_partners(request):
    partners_list = Person.objects.all()
    return render(request, 'partners_list.html', {'partners_list': partners_list, })

def not_allowed(request):
    return render(request, 'not_allowed.html',)