from django.template.loader import render_to_string

from conference_registration.forms import AddPartnerToConferenceList

from conference_registration.tasks import send_emails_task


class EmailSender:
    @staticmethod
    def get_message_data(request):
        form = AddPartnerToConferenceList(request.POST)
        if not form.is_valid():
            raise ValueError('Cannot send email, form is invalid')
        last_name = form.cleaned_data['last_name']
        first_name = form.cleaned_data['first_name']
        father_name = form.cleaned_data['father_name']
        company_inn = form.cleaned_data['company_inn']
        person_email = form.cleaned_data['person_email']
        person_phone = form.cleaned_data['person_phone']
        company_related_manager = form.cleaned_data['company_related_manager']
        return last_name, first_name, father_name, company_inn, person_email, person_phone, company_related_manager

    @classmethod
    def send_messages(cls, request, calculated_company_name):
        last_name, first_name, father_name, company_inn, person_email, person_phone, company_related_manager = cls.get_message_data(request)
        context = {
            'last_name': last_name,
            'first_name': first_name,
            'father_name': father_name,
            'company_inn': company_inn,
            'company_name': calculated_company_name,
            'person_email': person_email,
            'person_phone': person_phone,
            'company_related_manager': company_related_manager,
            }
        html_message_for_nda = render_to_string(
                'message_for_nda.html',
                context
            )
        html_message_for_customer = render_to_string(
                'message_for_customer.html',
                context)
        send_emails_task.delay(html_message_for_nda, html_message_for_customer, person_email, calculated_company_name)