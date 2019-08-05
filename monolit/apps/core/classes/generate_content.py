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


    def _get_objects_ids_list(self) -> list:
        return list(Object.objects.order_by('id').values_list('id', flat=True))


    def convert_tuple_to_flat_list(self, tuple):
        return [x[0] for x in tuple]


    def countBanks(self):
        return Bank.objects.all().count()


    def countOffers(self):
        return Offer.objects.all().count()


    def countFlatsInObject(self, object_id) -> int:
        return ObjectSite.objects.annotate(Count('object')).filter(object=object_id).count()


    """ [News] """


    """ [ObjectSite] """
    def _create_ObjectBathroom(self, object_site_id):
        object_bathroom_list = self.convert_tuple_to_flat_list(ObjectBathroom.BATHROOM_TYPES)
        count_bathrooms_rel_to_object_site = ObjectBathroom.objects.annotate(Count('object_site')).filter(object_site=object_site_id).count()

        object_site = ObjectSite.objects.get(pk=object_site_id)

        if count_bathrooms_rel_to_object_site == 0 or count_bathrooms_rel_to_object_site < 2:
            object_bathroom = ObjectBathroom(object_site=object_site, \
                                             bathroom_type=self.get_random_list_item(object_bathroom_list))
            object_bathroom.save()
            print(f'[ObjectBathroom] created for ObjectSite {object_site}')


    def _create_ObjectBalcony(self, object_site_id):
        object_balcony_list = self.convert_tuple_to_flat_list(ObjectBalcony.BALCONY_TYPES)
        count_balconies_rel_to_object_site = ObjectBalcony.objects.annotate(Count('object_site')).filter(object_site=object_site_id).count()

        object_site = ObjectSite.objects.get(pk=object_site_id)

        if count_balconies_rel_to_object_site == 0 or count_balconies_rel_to_object_site < 2:
            object_balcony = ObjectBalcony(object_site=object_site, \
                                           balcony_type=self.get_random_list_item(object_balcony_list))
            object_balcony.save()
            print(f'[ObjectBalcony] created for ObjectSite {object_site}')


    # Жилые объекты
    def _create_living_ObjectSite(self, object_id):
        site_types_list = self.convert_tuple_to_flat_list(ObjectSite.SITE_TYPES)
        site_types_list.remove('commercial')

        rooms_qty_list = self.convert_tuple_to_flat_list(ObjectSite.ROOMS_QTY)
        object = Object.objects.get(pk=object_id)

        # object_living = Object.objects.filter(category__id=1)
        # object_commercial = Object.objects.filter(category__id=2)
        # print(f'!!! Жилые объекты {object_living}')
        # print(f'!!! Коммерческие объекты {object_commercial}')

        floors_list = list(range(1, 23))
        site_numbers_list = list(range(100, 200))
        price_per_square_list = list(range(52000, 89000))
        site_area_list = list(range(57, 119))
        kitchen_area_list = list(range(10, 15))

        qty = 0
        if self.countFlatsInObject(object_id) == 0:
            qty = 100
        elif self.countFlatsInObject(object_id) < 100:
            qty = 100 - self.countFlatsInObject(object_id)

        for _ in range(qty):
            site_area = self.get_random_list_item(site_area_list)
            calc_living_area = site_area - 15

            object_site = ObjectSite(special_offer=self.fake.boolean(chance_of_getting_true=20), \
                                     object=object, \
                                     site_type=self.get_random_list_item(site_types_list), \
                                     crm_id=self.fake.random_number(9, True), \
                                     floor=self.get_random_list_item(floors_list), \
                                     site_number=self.get_random_list_item(site_numbers_list), \
                                     price_per_square=self.get_random_list_item(price_per_square_list), \
                                     rooms_qty=self.get_random_list_item(rooms_qty_list), \
                                     site_area=site_area, \
                                     living_area=calc_living_area, \
                                     kitchen_area=self.get_random_list_item(kitchen_area_list), \
                                     ceiling_height=2.7,\
                                    )
            object_site.save()
            print(f'[ObjectSite] {object_site.crm_id} created for Object {object_id}')

            # Add Balconies
            for _ in range(2):
                self._create_ObjectBalcony(object_site.id)

            # Add Batrooms
            for _ in range(2):
                self._create_ObjectBathroom(object_site.id)

        print(f'\nВ Объекте {object_id}, {self.countFlatsInObject(object_id)} квартир, было создано, {qty} квартир')


    # TODO: Generate commercial ObjectSite types


    """ [Mortgage] """
    def _create_Offer(self):
        # banks_ids = [1,2]
        banks_ids = list(Bank.objects.order_by('id').values_list('id', flat=True))
        bank = Bank.objects.get(pk=self.get_random_list_item(banks_ids))

        loan_term_from_list = [1, 3]
        loan_term_to_list = [25, 30]

        rate_from_list = [11.7, 11]
        rate_to_list = [11.7, 12]

        offer = Offer(bank=bank,\
                      title=f'Ипотечная программа {str(self.fake.word()).title()} {str(self.fake.random_number(4, True))}', \
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
        print(f'[Offer] {offer.title} created')


    def _create_Bank(self):
        if Bank.objects.all().count() > 0:
            print('[Bank] already created')
        else:
            bank = Bank(name='РНКБ', logo='img-placeholder.jpg')
            bank.save()

            bank = Bank(name='Банк Россия', logo='img-placeholder.jpg')
            bank.save()
            print('[Bank] are created')


    def _create_WayToBuy(self):
        objects_ids = self._get_objects_ids_list()
        way_to_buy = WayToBuy()

        if WayToBuy.objects.filter(pk=1).count() == 0:
            way_to_buy.save()
            way_to_buy.military.set(objects_ids)
            way_to_buy.mother.set(objects_ids)
            print(f'[WayToBuy] is created')
        else:
            way_to_buy = WayToBuy.objects.get(pk=1)
            way_to_buy.save()
            way_to_buy.military.set(objects_ids)
            way_to_buy.mother.set(objects_ids)
            print(f'[WayToBuy] is updated')


    """ [Object] """
    # x
    def _create_ObjectGalleryImage(self, gallery_id, qty: int):
        count_images_in_gallery = ObjectGalleryImage.objects.annotate(Count('gallery')).filter(gallery=gallery_id).count()

        if count_images_in_gallery == 0:
            gallery = ObjectGallery.objects.get(pk=gallery_id)

            for _ in range(qty):
                gallery_image = ObjectGalleryImage(gallery=gallery, image='img-placeholder.jpg')
                gallery_image.save()
            print(f'[GalleryImage] created for Gallery {gallery_id}')

    # x
    def _create_ObjectGallery(self, object_id, gal_names: list):
        count_object_galleries = ObjectGallery.objects.annotate(Count('object')).filter(object=object_id).count()

        if count_object_galleries == 0:
            object = Object.objects.get(pk=object_id)

            for gal_name in gal_names:
                object_gallery = ObjectGallery(object=object, name=gal_name)
                object_gallery.save()
                print(f'[Gallery "{gal_name}"] created for Object {object_id}')
                # Create gallery images
                self._create_ObjectGalleryImage(object_gallery.id, 7)

    # x
    def _create_ObjectDocumentAuthor(self):
        author_name = 'Иванов А.П.'
        count_object_document_authors = ObjectDocumentAuthor.objects.annotate(Count('name')).filter(name=author_name).count()

        if count_object_document_authors == 0:
            object_document_author = ObjectDocumentAuthor(name=author_name)
            object_document_author.save()
            print(f'[ObjectDocumentAuthor "{author_name}"] created')

    # x
    def _create_ObjectDocument(self, object_id, qty: int):
        count_documents_rel_to_object = ObjectDocument.objects.annotate(Count('object')).filter(object=object_id).count()

        if count_documents_rel_to_object == 0:
            for _ in range(qty):
                document_fake_title = f'Документ {self.fake.word()} {self.fake.word()} {self.fake.random_number(10, True)}'

                object = Object.objects.get(pk=object_id)
                object_document_author = ObjectDocumentAuthor.objects.first()

                object_document = ObjectDocument(object=object, title=document_fake_title, author=object_document_author)
                object_document.save()
                print(f'[ObjectDocument "{document_fake_title}"] created for Object {object_id}')

    # x
    def _create_ObjectElevator(self, object_section_id):
        count_elevators_rel_to_section = ObjectElevator.objects.annotate(Count('object_section')).filter(object_section=object_section_id).count()

        if count_elevators_rel_to_section == 0:
            elevator_types_list = self.convert_tuple_to_flat_list(ObjectElevator.ELEVATORS_TYPES)
            object_section = ObjectSection.objects.get(pk=object_section_id)

            object_elevator = ObjectElevator(object_section=object_section, \
                                             elevator_type=elevator_types_list[0], \
                                             elevator_qty=2
                                            )
            object_elevator.save()
            print(f'[ObjectElevator "{elevator_types_list[0]}"] created for ObjectSection {object_section_id}')

            object_elevator = ObjectElevator(object_section=object_section, \
                                             elevator_type=elevator_types_list[1], \
                                             elevator_qty=1
                                            )
            object_elevator.save()
            print(f'[ObjectElevator {elevator_types_list[1]}] created for ObjectSection {object_section_id}')

    # x
    def _create_ObjectSection(self, object_id):
        count_sections_rel_to_object = ObjectSection.objects.annotate(Count('object')).filter(object=object_id).count()

        if count_sections_rel_to_object == 0:
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
                                                floor_last=23, \
                                            )
                object_section.save()
                print(f'[ObjectSection "{object_section.name}"] created for Object {object_id}')
                i += 1
                # Create Elevators for Section
                self._create_ObjectElevator(object_section.id)

    # x
    def _create_ObjectBlock(self, object_id, qty: int):
        count_blocks_rel_to_object = ObjectBlock.objects.annotate(Count('object')).filter(object=object_id).count()

        if count_blocks_rel_to_object == 0:
            i = 1
            for _ in range(qty):
                block_name = f'Блок {i}'
                object = Object.objects.get(pk=object_id)
                object_block = ObjectBlock(object=object, name=block_name)
                object_block.save()
                print(f'[ObjectBlock "{block_name}"] created for Object {object_id}')
                i += 1

    # x
    def _create_ObjectInfoTab(self, object_id):
        count_info_tabs_rel_to_object = ObjectInfoTab.objects.annotate(Count('object')).filter(object=object_id).count()
        object_info_tab_icons_list = self.convert_tuple_to_flat_list(ObjectInfoTab.ICONS)
        object = Object.objects.get(pk=object_id)

        if count_info_tabs_rel_to_object == 0:
            for info_tab in object_info_tab_icons_list:
                object_info_tab = ObjectInfoTab(object=object, icon_name=info_tab, description=self.fake.text(300), image='img-placeholder.jpg')
                object_info_tab.save()
                print(f'[ObjectInfoTab "{info_tab}"] created for Object {object_id}')

    # x
    def _create_ObjectFile(self, object_id):
        count_files_rel_to_object = ObjectFile.objects.annotate(Count('object')).filter(object=object_id).count()
        file_types_list = self.convert_tuple_to_flat_list(ObjectFile.FILE_TYPES)

        if count_files_rel_to_object == 0:
            for file_type in file_types_list:
                object = Object.objects.get(pk=object_id)
                object_file = ObjectFile(object=object, name=file_type)
                object_file.save()
                print(f'[ObjectFile {file_type}] created for Object {object_id}')

    # x
    def _create_ObjectVideo(self, object_id, qty: int):
        count_videos_rel_to_object = ObjectVideo.objects.annotate(Count('object')).filter(object=object_id).count()

        if count_videos_rel_to_object == 0:
            for _ in range(qty):
                object = Object.objects.get(pk=object_id)
                object_video = ObjectVideo(object=object, video='https://www.youtube.com/watch?v=F5mRW0jo-U4')
                object_video.save()
                print(f'[ObjectVideo] created for Object {object_id}')

    # x
    def _create_Object(self):
        name = f'Объект {self.fake.word()} {self.fake.word()} {str(self.fake.random_number(4, True))}'.title()
        cities_list = self.convert_tuple_to_flat_list(Object.CITIES)

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
        # object.category.set([1])
        print(f'[Object] (ID: {object.id}) created "{name}"')


    def fillEntireSite(self, quantity):
        # 1. Create Objects
        for _ in range(quantity):
            self._create_Object()
        print('\n')

        # 2. Fill related to Objects models with content
        for object_id in self._get_objects_ids_list():
            self._create_ObjectVideo(object_id, 4)
            self._create_ObjectFile(object_id)
            self._create_ObjectInfoTab(object_id)
            self._create_ObjectBlock(object_id, 4)
            self._create_ObjectSection(object_id)
            self._create_ObjectGallery(object_id, ['Март 2019', 'Август 2019', 'Сентябрь 2019'])

        # 3. Fill Objects with Documents
        self._create_ObjectDocumentAuthor()

        for object_id in self._get_objects_ids_list():
            self._create_ObjectDocument(object_id, 23)

        # 4. Fill Mortgage
        self._create_WayToBuy()

        if self.countBanks() < 2:
            self._create_Bank()

        if self.countOffers() < 5:
            for _ in range(5 - self.countOffers()):
                self._create_Offer()

        # 5. Generate Flats and apartments
        for object_id in self._get_objects_ids_list():
            self._create_living_ObjectSite(object_id)
