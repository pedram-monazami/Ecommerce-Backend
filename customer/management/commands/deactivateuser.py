from argparse import ArgumentParser

from django.core.management import BaseCommand, CommandError

from customer.models import Customer


class Command(BaseCommand):
    help = 'A django command for activating users!'

    def add_arguments(self, parser: ArgumentParser):
        parser.add_argument('-u', '--username', default='Akbar', help='Enter username please')

    def handle(self, *args, **options):
        username = options['username']
        user = Customer.objects.get(user__username=username)
        if not user:
            raise CommandError(f"f{username} not found")
        if not user.is_active:
            raise CommandError(f"f{username} is already deactivated")
        user.is_active = False
        print(self.style.SUCCESS(f"{username} Deactivated"))
