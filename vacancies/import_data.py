from vacancies import data
from vacancies.models import Company, Specialty, Vacancy


def import_data():
    Vacancy.objects.all().delete()
    Specialty.objects.all().delete()
    Company.objects.all().delete()

    for speciality in data.specialties:
        Specialty.objects.create(
            code=speciality['code'],
            title=speciality['title'],
            picture=f'specty_{speciality["code"]}.png',
        )

    for company in data.companies:
        Company.objects.create(
            id_comp=company['id'],
            name=company['title'],
            location=company['location'],
            description=company['description'],
            employee_count=company['employee_count'],
            logo=f'media/static/logo{company["id"]}.png',
        )

    for job in data.jobs:
        specialty = Specialty.objects.get(code=job['specialty'])
        company = Company.objects.get(id_comp=job['company'])
        Vacancy.objects.create(
            id_job=job['id'],
            title=job['title'],
            specialty=specialty,
            company=company,
            description=job['description'],
            salary_min=int(job['salary_from']),
            salary_max=int(job['salary_to']),
            published_at=job['posted'],
        )


if __name__ == '__main__':
    import_data()
