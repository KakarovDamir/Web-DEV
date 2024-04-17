from django.urls import path
from . import views

urlpatterns = [
    path('hi/', views.hello),
    path('companies/', views.get_companies),
    path('companies/<int:pk>/', views.get_company),
    path('companies/<int:id>/vacancies/', views.get_company_vacancies),
    path('vacancies/', views.get_vacancies),
    path('vacancies/<int:pk>/', views.get_vacancy),
    path('vacancies/top_ten/', views.get_top_ten_vacancies),

]