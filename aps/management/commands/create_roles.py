from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        roles = ['Admin', 'Manager','Management', 'HR', 'Employee', 'Support']
        for role in roles:
            group, created = Group.objects.get_or_create(name=role)
            self.stdout.write(f"Role '{role}' created.")
