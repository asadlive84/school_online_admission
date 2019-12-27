from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from django.utils.text import slugify
from django.contrib.auth.decorators import login_required

from weasyprint import HTML, CSS
from weasyprint.fonts import FontConfiguration

from adminTools.models import SchoolInformation
from students.models import Student


# def student_admit_card_receipt(request, pk):
#     std = get_object_or_404(Student, pk=pk)
#     school_info = SchoolInformation.objects.all().last()
#     response = HttpResponse(content_type="application/pdf")
#     response['Content-Disposition'] = "inline; filename={name}-admit-card.pdf".format(
#         name=slugify(std.full_name_en))
#     html_string = render_to_string('students/create/create_admission_pdf.html', {
#         'std': std,
#         'school_info': school_info,
#     })
#
#     font_config = FontConfiguration()
#     HTML(string=html_string, base_url=request.build_absolute_uri()).write_pdf(response, font_config=font_config, presentational_hints=True)
#     return response


def student_admit_card_receipt(request, pk):
    std = Student.objects.get(pk=pk)
    school_info = SchoolInformation.objects.all().last()
    context = {
        'std': std, 'school_info': school_info,
    }
    html_string = render_to_string('students/create/create_admission_pdf.html', context).encode(encoding='UTF-8')
    html = HTML(string=html_string, base_url=request.build_absolute_uri('/'), encoding="UTF-8")
    pdf = html.write_pdf(presentational_hints=True)
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="mypdf.pdf"'
    return response
