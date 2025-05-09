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
            raise CommandError(f"{username} not found")
        if user.is_active:
            raise CommandError(f"{username} is already activated")
        user.is_active = True
        print(self.style.SUCCESS(f"{username} Activated"))
