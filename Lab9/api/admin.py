from django.contrib import admin

from api.models import Company, Vacancy

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'city', 'address')
    search_fields = ('name', 'description', 'city', 'address')


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'salary', 'company')
    search_fields = ('name', 'description','salary', 'company')