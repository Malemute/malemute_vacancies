from django.db import models
from django.db.models import CASCADE

from malemute_vacancies.settings import MEDIA_STATIC_DIR, MEDIA_SPECIALITY_DIR


class Company(models.Model):
    id_comp = models.IntegerField(default=0)
    name = models.CharField(max_length=60, default='')
    location = models.CharField(max_length=120, default='', null=True, blank=True)
    logo = models.ImageField(upload_to=MEDIA_STATIC_DIR, null=True, blank=True)
    description = models.TextField(default='', null=True, blank=True)
    employee_count = models.IntegerField(null=True, blank=True, default=0)

    def __str__(self):
        return f'{self.name}'


class Specialty(models.Model):
    code = models.CharField(max_length=20, default='', unique=True)
    title = models.CharField(max_length=40, default='')
    picture = models.ImageField(upload_to=MEDIA_SPECIALITY_DIR)

    def __str__(self):
        return f'{self.title}'


class Vacancy(models.Model):
    id_job = models.IntegerField(default=0)
    title = models.CharField(max_length=60)
    specialty = models.ForeignKey(Specialty, on_delete=CASCADE, related_name='vacancies')
    company = models.ForeignKey(Company, on_delete=CASCADE, related_name='vacancies')
    skills = models.TextField(default='', null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    salary_min = models.IntegerField(null=True, blank=True)
    salary_max = models.IntegerField(null=True, blank=True)
    published_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'
