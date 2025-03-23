from django.core.mail import EmailMessage

from datetime import datetime
from celery import shared_task

from nda.settings import EMAIL_HOST_USER, RECIPIENT_EMAIL


@shared_task
def send_emails_task(html_message_for_nda, html_message_for_customer, person_email, calculated_company_name):
    subject_for_nda = f'Новая регистрация на конференцию {calculated_company_name} {datetime.now().strftime("%Y-%m-%d %H:%M.")}'
    email_for_nda = EmailMessage(subject_for_nda,
                                 html_message_for_nda, EMAIL_HOST_USER, [RECIPIENT_EMAIL])
    subject_for_customer = f'Регистрация на конференцию НДА 2025 от {datetime.now().strftime("%Y-%m-%d %H:%M.")}'
    email_for_customer = EmailMessage(subject_for_customer,
                                      html_message_for_customer, EMAIL_HOST_USER, [person_email])
    email_for_nda.send(fail_silently=False)
    email_for_customer.send(fail_silently=False)