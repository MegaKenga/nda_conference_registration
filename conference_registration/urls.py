from django.urls import path

from conference_registration import views


urlpatterns = [
    path('add', views.person_add, name='person_add'),
    path('confirmation', views.confirmation, name='confirmation'),
    path('registered', views.list_partners, name='list_registered'),
]