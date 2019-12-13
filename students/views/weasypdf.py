from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from django.utils.text import slugify
from django.contrib.auth.decorators import login_required

from weasyprint import HTML
from weasyprint.fonts import FontConfiguration

from adminTools.models import SchoolInformation
from students.models import Student


def donation_receipt(request, pk):
    std = get_object_or_404(Student, pk=pk)
    school_info = SchoolInformation.objects.all().last()
    response = HttpResponse(content_type="application/pdf")
    response['Content-Disposition'] = "inline; filename={name}-donation-receipt.pdf".format(
        name=slugify(std.full_name_en))
    html = render_to_string('students/create/create_admission_pdf.html', {
        'std': std,
        'school_info': school_info,
    })

    font_config = FontConfiguration()
    HTML(string=html, base_url=request.build_absolute_uri()).write_pdf(response, font_config=font_config)
    return response
