from django.http import HttpResponse

from adminTools.models import SchoolInformation
from students.models import Student
from django.views.generic import DetailView

from students.views.std_barcode import MyBarcodeDrawing
import base64
from django.utils import timezone

from django.shortcuts import render

class StudentAdmissionPdf(DetailView):
    model = Student
    template_name = "students/create/admission_pdf.html"

    def barcode(self):
        text = "Hello friends"
        b = MyBarcodeDrawing(text)

        b.save(formats=['gif', 'pdf'], outDir = 'site_media/barcode/', fnRoot = 'barcode')
        barcodePicUrl = "barcode/barcode.gif"
        return barcodePicUrl

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['school'] = SchoolInformation.objects.all().last()
        context['barcode'] = self.barcode()
        context['printtime'] = timezone.now()
        return context
