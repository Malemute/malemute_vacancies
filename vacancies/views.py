from django.db.models import Count
from django.http import HttpResponseBadRequest, HttpResponseForbidden,  \
    HttpResponseNotFound, HttpResponseServerError
from django.shortcuts import get_object_or_404, render
from django.views import View
from django.views.generic import ListView

from vacancies.models import Company, Specialty, Vacancy


class MainView(View):
    def get(self, request, *args, **kwargs):
        specialties = Specialty.objects.all().annotate(number_of_vacancies=Count('vacancies'))
        companies = Company.objects.all()
        return render(request, 'vacancies/index.html', context={'specialties': specialties, 'companies': companies})


class VacancyListView(ListView):
    model = Vacancy
    template_name = 'vacancies/vacancies.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['vacancies'] = Vacancy.objects.all()
        return context


class VacancyCatView(View):
    def get(self, request, category_name):
        category_name = get_object_or_404(Specialty, code=category_name)
        vacancies = Vacancy.objects.filter(specialty=category_name)
        return render(
            request,
            'vacancies/vacancies.html',
            context={'category': category_name, 'vacancies': vacancies})


class CompanyView(View):
    def get(self, request, id_comp, *args, **kwargs):
        company = get_object_or_404(Company, id_comp=id_comp)
        vacancies = Vacancy.objects.filter(company=company)

        return render(
            request,
            'vacancies/company.html',
            context={'vacancies': vacancies, 'company': company})


class VacancyView(View):
    def get(self, request, id_job):
        vacancy = get_object_or_404(Vacancy, id_job=id_job)
        company = Company.objects.get(id=vacancy.company.id)
        return render(
            request,
            'vacancies/vacancy.html',
            context={
                'vacancy': vacancy,
                'company': company
            }
        )


def custom_handler400(request, exception):
    # Call when SuspiciousOperation raised
    return HttpResponseBadRequest('Неверный запрос!')


def custom_handler403(request, exception):
    # Call when PermissionDenied raised
    return HttpResponseForbidden('Доступ запрещен!')


def custom_handler404(request, exception):
    # Call when Http404 raised
    return HttpResponseNotFound('Ресурс не найден!')


def custom_handler500(request):
    # Call when raised some python exception
    return HttpResponseServerError('Ошибка сервера!')
