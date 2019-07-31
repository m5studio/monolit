""" README https://docs.djangoproject.com/en/dev/howto/custom-management-commands/ """

from django.core.management.base import BaseCommand, CommandError
from django.core.management import call_command
from django.conf import settings
from apps.core.classes.generate_content import GenerateContent
from apps.core.models import SiteSettings


"""
    TODO:
    x Check if site in DEBUG mode
    2. Add optional arguments for commend
"""


class Command(BaseCommand):
    help = 'Generate fake content with Faker'


    def add_arguments(self, parser):
        parser.add_argument('objects_qty', type=int, help='How many objects to create? (max 10)')


    def handle(self, *args, **options):
        if not settings.DEBUG:
            self.stdout.write(self.style.ERROR('You can\'t generate content in PRODUCTION mode, set DEBUG=True'))
        elif options['objects_qty'] > 10:
            self.stdout.write(self.style.ERROR('You can\'t generate more then 10 objects'))
        else:
            if SiteSettings.objects.all().count() == 0:
                print('!!!!!!!')
                # Call my command add_default_content automatically
                call_command('add_default_content')

            gen = GenerateContent()
            gen.fillEntireSite(options['objects_qty'])


    # self.stdout.write(self.style.ERROR('error message'))
    # self.stdout.write(self.style.SUCCESS('success message'))
    # self.stdout.write(self.style.WARNING('warning message'))
