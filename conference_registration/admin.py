from django.contrib import admin
# from django.contrib.admin import SimpleListFilter

from conference_registration.models import Person


# class CompanyNameFilter(SimpleListFilter):
#     title = 'Название компании партнера'
#     parameter_name = 'get_company_by_inn'
#     company_list = []
#     for person in Person.objects.all():
#         company = person.get_company_by_inn()
#         company_list.append(company)
#         set(company_list)
#     print(company_list)
#
#     def lookups(self, request, model_admin, company=None):
#         for company in self.company_list:
#             print(company)
#             return ((company, str(company)), )
#
#     def queryset(self, request, queryset):
#         if self.value() == "1":
#             return queryset.filter(external_number__isnull=False)
#         elif self.value() == "0":
#             return queryset.filter(external_number__isnull=True)
#         return queryset


class PersonAdmin(admin.ModelAdmin):
    list_display = (
        'last_name',
        'first_name',
        'father_name',
        'company_inn',
        'person_email',
        'person_phone',
        'company_related_manager',
        'get_company_by_inn'
    )
    list_filter = ('company_inn', 'company_related_manager', )
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
