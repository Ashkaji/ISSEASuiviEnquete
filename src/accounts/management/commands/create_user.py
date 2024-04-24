import csv
from django.core.management.base import BaseCommand
from accounts.models import CustomUser


class Command(BaseCommand):
    help = 'Loading file from the Survey Solution App Users file'

    def handle(self, *args, **options):
        with open('accounts/data/users.csv', 'r', encoding='utf-8') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for i, row in enumerate(csv_reader):
                if i > 0:
                    CustomUser.objects.create_user(
                        login=row[0],
                        password=row[1],
                        role=row[2],
                        supervisor=row[3],
                        fullname=row[4],
                    )
