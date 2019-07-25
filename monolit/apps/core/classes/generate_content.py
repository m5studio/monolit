from django.db.models import Count
# from django.conf import settings
from faker import Faker

from django.utils.text import slugify
from transliterate import translit

from apps.realty.models.object import Object, ObjectCategory
from apps.realty.models.object_video import ObjectVideo
from apps.realty.models.object_file import ObjectFile
from apps.realty.models.object_document import ObjectDocumentAuthor, ObjectDocument


class GenerateContent:
    def __init__(self):
        self.fake = Faker()


    def _get_objects_ids_list(self):
        return list(Object.objects.values_list('id', flat=True))


    def _create_ObjectDocumentAuthor(self):
        author_name = 'Иванов А.П.'
        count_object_document_authors = ObjectDocumentAuthor.objects.annotate(Count('name')).filter(name=author_name).count()

        if count_object_document_authors == 0:
            object_document_author = ObjectDocumentAuthor(name=author_name)
            object_document_author.save()
            print(f'ObjectDocumentAuthor {author_name} created')


    def _create_ObjectDocument(self, object_id, qty=30):
        count_object_document = ObjectDocument.objects.annotate(Count('object')).filter(object=object_id).count()

        if count_object_document == 0:
            for _ in range(qty):
                document_fake_title = f'Документ {self.fake.word()} {self.fake.word()} {self.fake.random_number(10, True)}'

                object = Object.objects.get(pk=object_id)
                object_document_author = ObjectDocumentAuthor.objects.first()
                # object_document_author = ObjectDocumentAuthor.objects.get(pk=2)
                object_document = ObjectDocument(object=object, title=document_fake_title, author=object_document_author)
                object_document.save()
                print(f'ObjectDocumentAuthor created {document_fake_title}')


    def _create_ObjectFile(self, object_id):
        count_files_rel_to_object = ObjectFile.objects.annotate(Count('object')).filter(object=object_id).count()

        file_types = ObjectFile.FILE_TYPES
        file_types_list = [x[0] for x in file_types]

        if count_files_rel_to_object == 0:
            for file_type in file_types_list:
                object = Object.objects.get(pk=object_id)
                object_file = ObjectFile(object=object, name=file_type)
                object_file.save()
                print(f'ObjectFile {file_type} created for Object {object_id}')


    def _create_ObjectVideo(self, object_id, qty=4):
        # Count videos in objects
        count_videos_rel_to_object = ObjectVideo.objects.annotate(Count('object')).filter(object=object_id).count()

        if count_videos_rel_to_object == 0:
            for _ in range(qty):
                object = Object.objects.get(pk=object_id)
                object_video = ObjectVideo(object=object, video='https://www.youtube.com/watch?v=F5mRW0jo-U4')
                object_video.save()
                print(f'ObjectVideo created for Object {object_id}')


    def _create_Object(self):
        fake = self.fake
        name = str('Объект ' + fake.word() + ' ' + fake.word() + ' ' + str(fake.random_number(4, True))).title()

        cities = Object.CITIES
        # Get every first item from cities tuple, and flatten to list
        cities_list = [x[0] for x in cities]

        object = Object(completed=fake.boolean(chance_of_getting_true=40), \
                        all_sold=fake.boolean(chance_of_getting_true=30), \
                        crm_id=fake.random_number(7, True), \
                        name=name, \
                        slug=slugify(translit(name, 'ru', reversed=True)), \
                        description=fake.text(1000), \
                        object_type='living_complex', \
                        building_type='monolith', \
                        city=fake.word(cities_list),\
                        genplan='img-placeholder.jpg', \
                        main_image='img-placeholder.jpg', \
                        webcam='https://rtsp.me/embed/3KASrTkG/', \
                        panoram='https://monolit360.com/files/main/index.html?s=pano1692', \
                    )
        object.save()

        # Set ManyToMany categories
        object.category.set([1, 2])

        print(f'\nObject created {name}')

        self._create_ObjectDocumentAuthor()

        for object_id in self._get_objects_ids_list():
            self._create_ObjectVideo(object_id)
            self._create_ObjectFile(object_id)
            self._create_ObjectDocument(object_id)
