from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from dotenv import load_dotenv

from conference_registration.models import Person
from conference_registration.forms import AddPartnerToConferenceList, LoginUserForm
from conference_registration.email_sender import EmailSender


load_dotenv()


def index(request):
    return render(request, 'index.html')


def person_add(request):
    if request.method == 'POST':
        form = AddPartnerToConferenceList(request.POST)
        if form.is_valid():
            try:
                EmailSender.send_messages(request)
                Person.objects.create(**form.cleaned_data)
            except Exception as e:
                print(f'email_send failed due to: {e}')
                response = HttpResponse(status=500)
                return response
            return redirect('confirmation')
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