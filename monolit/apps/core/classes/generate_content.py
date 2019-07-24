from django.db.models import Count
# from django.conf import settings
from faker import Faker

from django.utils.text import slugify
from transliterate import translit

from apps.realty.models.object import Object, ObjectCategory
from apps.realty.models.object_video import ObjectVideo
from apps.realty.models.object_file import ObjectFile


class GenerateContent:
    def __init__(self):
        self.fake = Faker()


    def _get_objects_ids_list(self):
        return list(Object.objects.values_list('id', flat=True))


    def _create_object_file(self, object_id):
        count_files_rel_to_object = ObjectFile.objects.annotate(Count('object')).filter(object=object_id).count()

        file_types = ObjectFile.FILE_TYPES
        file_types_list = [x[0] for x in file_types]

        if count_files_rel_to_object == 0:
            for file_type in file_types_list:
                object = Object.objects.get(pk=object_id)
                object_file = ObjectFile(object=object, name=file_type)
                object_file.save()


    def _create_object_video(self, object_id, qty=4):
        # Count ideos in objects
        count_videos_rel_to_object = ObjectVideo.objects.annotate(Count('object')).filter(object=object_id).count()

        if count_videos_rel_to_object == 0:
            for _ in range(qty):
                object = Object.objects.get(pk=object_id)
                object_video = ObjectVideo(object=object, video='https://www.youtube.com/watch?v=F5mRW0jo-U4')
                object_video.save()


    def _create_object(self):
        fake = self.fake
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
        print('[Created Object ID]: ' + str(object.id) + ' ' + name)

        for object_id in self._get_objects_ids_list():
            self._create_object_video(object_id)
            self._create_object_file(object_id)
