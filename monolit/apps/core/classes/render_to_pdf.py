from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
import xhtml2pdf.pisa as pisa


class RenderToPDF:

    @staticmethod
    def render(path: str, params: dict, filename='my_filename'):
        template = get_template(path)
        html = template.render(params)
        response = BytesIO()
        pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), response)
        if not pdf.err:
            # return HttpResponse(response.getvalue(), content_type='application/pdf')
            resp = HttpResponse(response.getvalue(), content_type='application/pdf')
            resp['Content-Disposition'] = f'inline; filename={filename}.pdf'
            return resp
        else:
            return HttpResponse("Error Rendering PDF", status=400)
