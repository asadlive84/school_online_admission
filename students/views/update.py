from django.views.generic import UpdateView
from students.models import Student


class StudentUpdateView(UpdateView):
    model = Student
    template_name = "students/update/student_update.html"
    fields = "__all__"
