""" README https://docs.djangoproject.com/en/dev/howto/custom-management-commands/ """

from django.core.management.base import BaseCommand, CommandError

from django.conf import settings
from faker import Faker

from django.utils.text import slugify
from transliterate import translit

from apps.realty.models.object import Object, ObjectCategory


"""
    TODO:
    x Check if site in DEBUG mode
    2. Add optional arguments for commend
"""


class Command(BaseCommand):
    help = 'Generate fake content with Faker'

    def add_arguments(self, parser):
        parser.add_argument('objects_qty', type=int, help='How many objects to create?')


    def _create_object(self):
        fake = Faker()
        name = str('Объект ' + fake.word() + ' ' + fake.word() + ' ' + str(fake.random_number(4, True))).title()

        cities = Object.CITIES
        # Get every first item from cities tuple, and flatten to list
        cities_list = [x[0] for x in cities]

        object = Object.objects.create(completed=fake.boolean(chance_of_getting_true=40), \
                                        all_sold=fake.boolean(chance_of_getting_true=30), \
                                        crm_id=fake.random_number(7, True), \
                                        name=name, \
                                        slug=slugify(translit(name, 'ru', reversed=True)), \
                                        description=fake.text(1000), \
                                        object_type='living_complex', \
                                        building_type='monolith', \
                                        city=fake.word(cities_list),\
                                        webcam='https://rtsp.me/embed/3KASrTkG/', \
                                        panoram='https://monolit360.com/files/main/index.html?s=pano1692', \
                                    )
        # Set ManyToMany categories
        object.category.set([1, 2])
        self.stdout.write(self.style.SUCCESS('[Created Object]: ' + name))


    def handle(self, *args, **options):
        if not settings.DEBUG:
            self.stdout.write(self.style.ERROR('You can\'t generate content in PRODUCTION mode, set DEBUG=True'))
        else:
            i = 0
            for _ in range(options['objects_qty']):
                self._create_object()
                self.stdout.write(self.style.SUCCESS(i++))

    # self.stdout.write(self.style.ERROR('error message'))
    # self.stdout.write(self.style.SUCCESS('success message'))
    # self.stdout.write(self.style.WARNING('warning message'))
