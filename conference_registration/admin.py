from django.contrib import admin
from conference_registration.models import Person

class PersonAdmin(admin.ModelAdmin):
    list_display = (
        'last_name',
        'first_name',
        'father_name',
        'company_inn',
        'person_email',
        'person_phone',
        'company_related_manager',
    )
    list_filter = ('company_inn', )
    fields = [
        'last_name',
        'first_name',
        'father_name',
        'company_inn',
        'person_email',
        'person_phone',
        'company_related_manager',
    ]
    view_on_site = True
    actions_on_bottom = True
    list_per_page = 25
    search_fields = ['last_name', 'company_inn', 'company_related_manager']


admin.site.register(Person, PersonAdmin)
