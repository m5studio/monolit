""" README https://docs.djangoproject.com/en/dev/howto/custom-management-commands/ """

from django.core.management.base import BaseCommand, CommandError

from django.conf import settings
from apps.core.classes.generate_content import GenerateContent


"""
    TODO:
    x Check if site in DEBUG mode
    2. Add optional arguments for commend
"""


class Command(BaseCommand):
    help = 'Generate fake content with Faker'


    def add_arguments(self, parser):
        parser.add_argument('objects_qty', type=int, help='How many objects to create?')


    def handle(self, *args, **options):
        if not settings.DEBUG:
            self.stdout.write(self.style.ERROR('You can\'t generate content in PRODUCTION mode, set DEBUG=True'))
        else:
            for _ in range(options['objects_qty']):
                gen = GenerateContent()
                gen._create_object()


    # self.stdout.write(self.style.ERROR('error message'))
    # self.stdout.write(self.style.SUCCESS('success message'))
    # self.stdout.write(self.style.WARNING('warning message'))
