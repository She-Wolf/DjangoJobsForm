from django.http import HttpResponseNotFound, HttpResponseServerError, Http404
from django.shortcuts import render
from jobs.models import Specialty, Vacancy,Company


def custom_handler404(request, exception):
    return HttpResponseNotFound('Ой, что-то пошло не так...Проверьте, что ввели ')


def custom_handler500(request):
    return HttpResponseServerError('Сервер прилег... Скоро починим')


def index(request):
    specialities = Specialty.objects.all()
    companies = Company.objects.all()
    speciality_vacancies_count = []
    # for speciality in specialities:
    #     speciality_vacancies = Vacancy.objects.filter(specialty = speciality.pk)
    #     speciality_vacancies_count[speciality] = speciality_vacancies.count()

    return render(request, 'index.html',{'specialities':specialities,
                                         'companies':companies,
                                         # 'speciality_vacancies_count':speciality_vacancies_count
                                         })

def vacancies(request):
    vacancies = Vacancy.objects.all()
    vacancies_count = Vacancy.objects.count()
    return render(request, 'vacancies.html',{'vacancies':vacancies,
                                             'vacancies_count':vacancies_count})

def speciality(request,speciality_name):

    return render(request, 'speciality.html')

def company(request, company_id):
    return render(request, 'company.html',{})

def vacancy(request, vacancy_id):
    vacancy = Vacancy.objects.get(id = vacancy_id)
    skills = vacancy.skills.replace(",", " • ")
    return render(request, 'vacancy.html',{'vacancy':vacancy,
                                           'skills':skills})