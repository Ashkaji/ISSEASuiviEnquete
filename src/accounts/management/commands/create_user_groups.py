from django.contrib.auth.models import Group
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Creates Django groups for user types (Interviewers, Controllers, etc.)'

    def handle(self, *args, **options):
        group_names = ['Interviewers', 'Supervisors', 'Headquarters', 'Observers']
        for name in group_names:
            group, created = Group.objects.get_or_create(name=name)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Group "{name}" created.'))
            else:
                self.stdout.write(self.style.WARNING(f'Group "{name}" already exists.'))
