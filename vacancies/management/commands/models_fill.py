from django.core.management.base import BaseCommand

from vacancies.import_data import import_data


class Command(BaseCommand):
    help = 'Fills the models'

    def handle(self, *args, **options):
        import_data()
