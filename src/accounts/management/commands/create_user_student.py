import csv

from django.core.management.base import BaseCommand
from django.db import transaction
from accounts.models import StudentUser


class Command(BaseCommand):
    help = 'Bulk creates or updates data in your app.'

    def add_arguments(self, parser):
        parser.add_argument('--action', type=str, required=True, choices=['create', 'update'],
                            help='Specify the action to perform: create or update data.')
        parser.add_argument('--data_file', type=str, required=True,
                            help='Path to the CSV file containing bulk data.')

    def handle(self, *args, **options):
        action = options['action']
        data_file = options['data_file']

        if action == 'create':
            self.bulk_create_data(data_file)
        elif action == 'update':
            self.bulk_update_data(data_file)
        else:
            raise ValueError(f'Invalid action: {action}')

    def bulk_create_data(self, data_file):
        with open(data_file, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                with transaction.atomic():  # Keep each object creation within a transaction
                    StudentUser.objects.create_user(**row)

        self.stdout.write(self.style.SUCCESS(f'Successfully created StudentUser objects.'))

    def bulk_update_data(self, data_file):
        with open(data_file, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)

            update_data = []
            for row in reader:
                student_id = row['id']  # Assuming 'id' is the unique identifier column
                update_values = {field: row[field] for field in row.keys() if field != 'id'}
                update_data.append((student_id, update_values))

        with transaction.atomic():
            # Efficient bulk update using filter & update_qs
            pks = [item[0] for item in update_data]  # Extract all IDs for filtering

            try:
                # Attempt bulk update using filter & update_qs
                StudentUser.objects.filter(pk__in=pks).update(**update_data[0][1])
            except Exception as e:
                # Handle potential exception (e.g., database errors)
                self.stdout.write(self.style.ERROR(f'Error during bulk update: {e}'))
