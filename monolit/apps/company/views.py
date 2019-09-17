import os, zipfile
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from apps.core.classes.file_processing import FileProcessing

from apps.company.models.certificate import Certificate
from apps.company.models.management import Management
from apps.company.models.responsibility import Responsibility
from apps.company.models.job import JobBlock, JobVacancy
from apps.company.models.history import History
from apps.company.models.structure import Structure
from apps.company.models.partner import Partner
from apps.company.models.tender import Tender, TenderFile
from apps.realty.models.object import Object


class CompanyView(TemplateView):
    template_name = 'company/company.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_tite'] = 'О компании'
        context['certificates'] = Certificate.objects.all()
        return context


class CompanyMissionView(TemplateView):
    template_name = 'company/company_mission.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_tite'] = 'Миссия и ценности'
        return context


class CompanyManagementView(TemplateView):
    template_name = 'company/company_management.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_tite'] = 'Менеджмент'
        context['management'] = Management.objects.all().order_by('order')
        return context


class CompanyResponsibilityView(TemplateView):
    template_name = 'company/company_responsibility.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_tite'] = 'Социальная ответственность'
        context['responsibilities'] = Responsibility.objects.all().order_by('order')
        return context


class CompanyJobView(TemplateView):
    template_name = 'company/company_job.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_tite'] = 'Работа в компании'
        context['job_blocks'] = JobBlock.objects.all().order_by('order')
        context['job_vacancies'] = JobVacancy.objects.all().order_by('order')
        return context


class CompanyHistory(TemplateView):
    template_name = 'company/company_history.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_tite'] = 'История компании'
        context['history'] = History.objects.all().order_by('-year')
        return context


class CompanyStructure(TemplateView):
    template_name = 'company/company_structure.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_tite'] = 'Стурктура компании'
        context['structure'] = Structure.objects.all().order_by('order')
        return context


class CompanyPartnership(TemplateView):
    template_name = 'company/company_partnership.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_tite'] = 'Партнерская программа'
        context['partners'] = Partner.objects.all().order_by('order')
        context['objects_partnership'] = Object.objects.filter(active=True, partnership=True).order_by('?')
        return context


class CompanyTenders(TemplateView):
    template_name = 'company/company_tenders.html'

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_tite'] = 'Тендеры'
        context['tenders_categories'] = Tender.CATEGORIES
        context['tender_files'] = TenderFile.objects.all()
        context['tenders'] = Tender.objects.all().order_by('-active', 'date_end')

        # Query ?tender_category= processing
        if request.GET.get('tender_category'):
            context['tenders'] = Tender.objects.filter(category=request.GET.get('tender_category')).order_by('-active', 'date_end')
        if request.GET.get('tender_category') == 'all':
            context['tenders'] = Tender.objects.all().order_by('-active', 'date_end')

        # Download all files related to tender
        get_request_tender_id = request.GET.get('download-all-tender-files')
        if get_request_tender_id:
            file_paths = list()
            for root, directories, files in os.walk( './media/company/tenders/{}'.format(get_request_tender_id) ):
                for filename in files:
                    filepath = os.path.join(root, filename)
                    file_paths.append(filepath)

            response = HttpResponse(content_type='application/zip')
            # response = HttpResponse(content_type='application/octet-stream')
            # response = HttpResponse(content_type='application/x-zip-compressed')

            zip_file = zipfile.ZipFile(response, 'w')

            with zipfile.ZipFile(response, 'w') as zip:
                # writing each file one by one
                for file in file_paths:
                    # basename to avoid directory structure
                    zip.write(file, os.path.basename(file))

                # new_filename = 'monolit_tender_{}.zip'.format(get_request_tender_id)

                tender_title = Tender.objects.filter(id=get_request_tender_id).values_list('title', flat=True)
                # print(tender_title[0])
                filename = FileProcessing(tender_title[0])
                # filename = filename.newFileNameTranslitSlugify().title()
                filename = filename.translitFileName().title() 
                new_filename = '[monolit.site] tender_{id} {filename}.zip'.format(filename=filename, id=get_request_tender_id)

                response['Content-Disposition'] = 'attachment; filename="{filename}"'.format(filename=new_filename)
                return response
        # END Download all files related to tender

        # Object Documents Pagination
        paginator = Paginator(context['tenders'], 5)
        page_docs = self.request.GET.get('page')
        try:
            context['tenders'] = paginator.page(page_docs)
        except PageNotAnInteger:
            context['tenders'] = paginator.page(1)
        except EmptyPage:
            context['tenders'] = paginator.page(paginator.num_pages)
        # END Object Documents Pagination

        return render(request, self.template_name, context)
