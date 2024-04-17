from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from api.models import Company, Vacancy
from django.shortcuts import get_object_or_404

def hello(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def get_companies(request):
    companies = Company.objects.all()
    companies_json = [company.to_json() for company in companies]
    return JsonResponse(companies_json, safe=False)

def get_company(request, pk = None):
    try:
        company = Company.objects.get(id=pk)
        return JsonResponse(company.to_json())
    
    except Company.DoesNotExist as e:
        return JsonResponse({
            'error': str(e)
         })
    
def get_vacancies(request):
    varancies = Vacancy.objects.all()
    varancies_json = [varancy.to_json() for varancy in varancies]
    return JsonResponse(varancies_json, safe=False)

def get_vacancy(request, pk = None):
    try:
        varancy = Vacancy.objects.get(id=pk)
        return JsonResponse(varancy.to_json())

    except Vacancy.DoesNotExist as e:
        return JsonResponse({
            'error': str(e)
         })
    

def get_top_ten_vacancies(request, pk = None):
    vacancies = Vacancy.objects.order_by('-salary')[:10]
    vacancies_json = [vacancy.to_json() for vacancy in vacancies]
    return JsonResponse(vacancies_json, safe=False)

def get_company_vacancies(request, id):
    company = get_object_or_404(Company, id=id)
    vacancies = company.vacancy_set.all()
    vacancies_json = [vacancy.to_json() for vacancy in vacancies]
    return JsonResponse(vacancies_json, safe=False)