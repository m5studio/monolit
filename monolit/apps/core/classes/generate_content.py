import random

from django.db.models import Count
# from django.conf import settings
from faker import Faker

from django.utils.text import slugify
from transliterate import translit

from apps.realty.models.object import Object, ObjectCategory
from apps.realty.models.object_video import ObjectVideo
from apps.realty.models.object_file import ObjectFile
from apps.realty.models.object_document import ObjectDocumentAuthor, ObjectDocument
from apps.realty.models.object_info_tab import ObjectInfoTab
from apps.realty.models.object_block import ObjectBlock
from apps.realty.models.object_section import ObjectSection
from apps.realty.models.object_elevator import ObjectElevator
from apps.realty.models.object_gallery import ObjectGallery, ObjectGalleryImage

from apps.mortgage.models import WayToBuy, Bank, Offer

from apps.realty.models.object_site import ObjectSite, ObjectSiteWindowsView
from apps.realty.models.object_site_balcony import ObjectBalcony
from apps.realty.models.object_site_bathroom import ObjectBathroom


class GenerateContent:
    def __init__(self):
        self.fake = Faker()


    def get_random_list_item(self, list):
        return random.choice(list)


    def _get_objects_ids_list(self):
        return list(Object.objects.values_list('id', flat=True))


    # TODO: News
    """ [News] """


    """ [ObjectSite] """
    
    # TODO: Generate commercial Object types

    def _create_ObjectSite(self, object_id):
        site_types = ObjectSite.SITE_TYPES
        site_types_list = [x[0] for x in site_types]
        site_types_list.remove('commercial')

        rooms_qty = ObjectSite.ROOMS_QTY
        rooms_qty_list = [x[0] for x in rooms_qty]

        object = Object.objects.get(pk=object_id)

        object_site = ObjectSite(special_offer=self.fake.boolean(chance_of_getting_true=20), \
                                 object=object, \
                                 site_type=self.get_random_list_item(site_types_list), \
                                 crm_id=self.fake.random_number(9, True), \
                                 floor=5, \
                                 site_number=19, \
                                 price_per_square=57000, \
                                 rooms_qty=self.get_random_list_item(rooms_qty_list), \
                                 site_area=67, \
                                )
        object_site.save()
        print(f'ObjectSite {object_site.crm_id} created')




    """ [Mortgage] """
    def _create_mortgage_Offer(self):
        banks_ids = [1, 2]
        bank = Bank.objects.get(pk=self.get_random_list_item(banks_ids))
        # bank = Bank.objects.get(pk=1)

        loan_term_from_list = [1, 3]
        loan_term_to_list = [25, 30]

        rate_from_list = [11.7, 11]
        rate_to_list = [11.7, 12]

        offer = Offer(bank=bank,\
                      title=f'Название программы {str(self.fake.word()).title()} {str(self.fake.random_number(4, True))}', \
                      first_payment_from=15, \
                      first_payment_to=15, \
                      loan_term_from=self.get_random_list_item(loan_term_from_list), \
                      loan_term_to=self.get_random_list_item(loan_term_to_list), \
                      rate_from=self.get_random_list_item(rate_from_list), \
                      rate_to=self.get_random_list_item(rate_to_list), \
                      description=self.fake.text(500)
                    )
        offer.save()

        objects_ids_list = list(self._get_objects_ids_list())
        offer.object.set(objects_ids_list)
        print(f'Mortgage offer {offer.title} created')


    def _create_mortgage_Banks(self):
        if Bank.objects.all().count() > 0:
            print('Banks already created')
        else:
            bank = Bank(name='РНКБ', logo='img-placeholder.jpg')
            bank.save()
            bank = Bank(name='Банк Россия', logo='img-placeholder.jpg')
            bank.save()
            print('Banks are created')


    def _create_mortgage_WayToBuy(self):
        objects_ids = self._get_objects_ids_list()
        way_to_buy = WayToBuy()

        if WayToBuy.objects.filter(pk=1).count() == 0:
            way_to_buy.save()
            way_to_buy.military.set(objects_ids)
            way_to_buy.mother.set(objects_ids)
            print(f'WayToBuy is created')
        else:
            way_to_buy = WayToBuy.objects.get(pk=1)
            way_to_buy.save()
            way_to_buy.military.set(objects_ids)
            way_to_buy.mother.set(objects_ids)
            print(f'WayToBuy is updated')


    """ [Object] """
    def _create_ObjectGalleryImage(self, gallery_id):
        count_images_in_gallery = ObjectGalleryImage.objects.annotate(Count('gallery')).filter(gallery=gallery_id).count()

        if count_images_in_gallery == 0:
            gallery = ObjectGallery.objects.get(pk=gallery_id)

            for _ in range(7):
                gallery_image = ObjectGalleryImage(gallery=gallery, image='img-placeholder.jpg')
                gallery_image.save()
            print(f'Add gallery images for gallery {gallery_id}')


    def _create_ObjectGallery(self, object_id):
        count_object_galleries = ObjectGallery.objects.annotate(Count('object')).filter(object=object_id).count()

        gal_names = ['Март 2019', 'Июль 2019', 'Сентябрь 2019']

        if count_object_galleries == 0:
            object = Object.objects.get(pk=object_id)

            for gal_name in gal_names:
                object_gallery = ObjectGallery(object=object, name=gal_name)
                object_gallery.save()
                print(f'Gallery {gal_name} created for Object {object_id}')

                # Create gallery images
                self._create_ObjectGalleryImage(object_gallery.id)


    # TODO: create elevators
    def _create_ObjectElevator(self, object_section_id):
        elevator_types = ObjectElevator.ELEVATORS_TYPES
        elevator_types_list = [x[0] for x in elevator_types]

        object_section = ObjectSection.objects.get(pk=object_section_id)

        object_elevator = ObjectElevator(object_section=object_section, \
                                         elevator_type=elevator_types_list[0], \
                                         elevator_qty=2
                                        )
        object_elevator.save()
        print(f'ObjectElevator {elevator_types_list[0]} created')

        object_elevator = ObjectElevator(object_section=object_section, \
                                         elevator_type=elevator_types_list[1], \
                                         elevator_qty=1
                                        )
        object_elevator.save()
        print(f'ObjectElevator {elevator_types_list[1]} created')


    def _create_ObjectSection(self, object_id):
        count_object_sections = ObjectSection.objects.annotate(Count('object')).filter(object=object_id).count()

        if count_object_sections == 0:
            object_blocks_ids = ObjectBlock.objects.filter(object=object_id).values_list('id', flat=True)

            i = 1
            for object_block_id in object_blocks_ids:
                object = Object.objects.get(pk=object_id)
                object_block = ObjectBlock.objects.filter(object=object_id).get(pk=object_block_id)
                object_section = ObjectSection(object=object, \
                                                object_block=object_block, \
                                                number=self.fake.random_number(3, True), \
                                                name=f'Секция {i}', \
                                                floor_first=1, \
                                                floor_last=23
                                            )
                object_section.save()
                print(f'ObjectSection Секция {i} created')
                i += 1

                # Create Elevators for Section
                self._create_ObjectElevator(object_section.id)



    def _create_ObjectBlock(self, object_id):
        count_object_blocks = ObjectBlock.objects.annotate(Count('object')).filter(object=object_id).count()

        if count_object_blocks == 0:
            i = 1
            for _ in range(4):
                block_name = f'Блок {i}'

                object = Object.objects.get(pk=object_id)
                object_block = ObjectBlock(object=object, name=block_name)
                object_block.save()

                print(f'ObjectBlock {block_name} created for Object {object_id}')
                i += 1


    def _create_ObjectInfoTab(self, object_id):
        count_object_info_tabs = ObjectInfoTab.objects.annotate(Count('object')).filter(object=object_id).count()

        object_info_tab_icons = ObjectInfoTab.ICONS
        object_info_tab_icons_list = [x[0] for x in object_info_tab_icons]

        if count_object_info_tabs == 0:
            for info_tab in object_info_tab_icons_list:
                object = Object.objects.get(pk=object_id)
                object_info_tab = ObjectInfoTab(object=object, icon_name=info_tab, description=self.fake.text(300), image='img-placeholder.jpg')
                object_info_tab.save()
                print(f'ObjectInfoTab {info_tab} created for Object {object_id}')


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
        name = f'Объект {self.fake.word()} {self.fake.word()} {str(self.fake.random_number(4, True))}'.title()
        cities = Object.CITIES

        # Get every first item from cities tuple, and flatten to list
        cities_list = [x[0] for x in cities]

        object = Object(completed=self.fake.boolean(chance_of_getting_true=40), \
                        all_sold=self.fake.boolean(chance_of_getting_true=30), \
                        crm_id=self.fake.random_number(7, True), \
                        name=name, \
                        slug=slugify(translit(name, 'ru', reversed=True)), \
                        description=self.fake.text(1000), \
                        object_type='living_complex', \
                        building_type='monolith', \
                        city=self.fake.word(cities_list),\
                        address='ул. Ленина 12', \
                        genplan='img-placeholder.jpg', \
                        main_image='img-placeholder.jpg', \
                        webcam='https://rtsp.me/embed/3KASrTkG/', \
                        panoram='https://monolit360.com/files/main/index.html?s=pano1692', \
                    )
        object.save()

        # Set ManyToMany categories
        object.category.set([1, 2])

        print(f'\n=========[Object [ID: {object.id}] created: "{name}"]=========')


    def fillEntireSite(self, quantity):
        for _ in range(quantity):
            self._create_Object()
            self._create_ObjectDocumentAuthor()

            self._create_mortgage_WayToBuy()
            self._create_mortgage_Banks()
            # self._create_mortgage_Offer()

            for object_id in self._get_objects_ids_list():
                self._create_ObjectVideo(object_id)
                self._create_ObjectFile(object_id)
                self._create_ObjectDocument(object_id)
                self._create_ObjectInfoTab(object_id)
                self._create_ObjectGallery(object_id)
                self._create_ObjectBlock(object_id)
                self._create_ObjectSection(object_id)

        if Offer.objects.all().count() < 6:
            for _ in range(6):
                self._create_mortgage_Offer()

        for object_id in self._get_objects_ids_list():
            for _ in range(quantity * 10):
                self._create_ObjectSite(object_id)