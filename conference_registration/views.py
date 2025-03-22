from dadata import Dadata
from dotenv import load_dotenv
import os

from django.shortcuts import render, redirect

from conference_registration.models import Person
from conference_registration.forms import AddPartnerToConferenceList

load_dotenv()


def get_company_by_inn(inn):
    inn = Person.company_inn
    token = os.getenv('TOKEN')
    dadata = Dadata(token)
    result = dadata.find_by_id(name="party", query=str(inn))

    for name in result:
        return(name['value'])


def person_add(request):
    if request.method == 'POST':
        form = AddPartnerToConferenceList(request.POST)
        if form.is_valid():
            try:
                Person.objects.create(**form.cleaned_data)
            except:
                form.add_error(None, 'Ошибка добавления поста')
            form.save()
            return redirect('confirmation')
    else:
        form = AddPartnerToConferenceList()
    return render(request, 'addperson.html', {'form': form})


def confirmation(request):
    return render(request, 'confirmation.html')