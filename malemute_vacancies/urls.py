"""malemute_vacancies URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from vacancies.views import CompanyView
from vacancies.views import MainView
from vacancies.views import VacancyCatView
from vacancies.views import VacancyListView
from vacancies.views import VacancyView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainView.as_view(), name='main_page'),
    path('vacancies/', VacancyListView.as_view(), name='vacancies_page'),
    path('vacancies/cat/<str:category_name>', VacancyCatView.as_view(), name='category_page'),
    path('companies/<int:id_comp>', CompanyView.as_view(), name='company_page'),
    path('vacancies/<int:id_job>', VacancyView.as_view(), name='vacancy_info'),

]
