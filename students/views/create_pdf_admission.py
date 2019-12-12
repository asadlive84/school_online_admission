from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
import xhtml2pdf.pisa as pisa
from django.views.generic import View, DetailView
from django.utils import timezone

from students.models import Student


class Render:

    @staticmethod
    def render(path: str, params: dict):
        template = get_template(path)
        html = template.render(params)
        response = BytesIO()
        pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), response)
        if not pdf.err:
            return HttpResponse(response.getvalue(), content_type='application/pdf')
        else:
            return HttpResponse("Error Rendering PDF", status=400)


class Pdf(View):
    model = Student

    def get(self, request, *args, **kwargs):
        std = Student.objects.get(pk=self.kwargs.get('pk'))
        today = timezone.now()
        params = {
            'today': today,
            'sales': std,
            'request': request
        }
        return Render.render('students/create/create_admission_pdf.html', params)
